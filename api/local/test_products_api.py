import json
from pathlib import Path

import pytest
import requests
from jsonschema import validate

BASE_DIR = Path(__file__).resolve().parents[2]
SCHEMAS_DIR = BASE_DIR / "api" / "schemas"

BASE_URL = "http://127.0.0.1:8000"

def load_schema(filename):
    schema_path = SCHEMAS_DIR / filename
    with schema_path.open(encoding="utf-8") as file:
        schema = json.load(file)

    return schema

product_schema = load_schema("product.json")
message_schema = load_schema("message.json")


@pytest.fixture
def created_product():
    payload = {
        "name": "Mouse",
        "price": 1500
    }

    response = requests.post(
        f"{BASE_URL}/products",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()
    assert isinstance(data, dict)

    yield data

    response = requests.delete(
        f"{BASE_URL}/products/{data['id']}",
        timeout=10
    )
    assert response.status_code == 200
    response_get = requests.get(f"{BASE_URL}/products/{data['id']}",
            timeout=10)
    assert response_get.status_code == 404
    data_get = response_get.json()
    assert isinstance(data_get, dict)
    assert "Product not found" in data_get['detail']


def test_get_created_product(created_product):
    url = f"{BASE_URL}/products/{created_product['id']}"

    response = requests.get(url, timeout=10)

    assert response.status_code == 200

    data = response.json()
    validate(data, product_schema)

    assert data['id'] == created_product['id']
    assert data['name'] == created_product['name']
    assert data['price'] == created_product['price']

def test_update_product(created_product):
    url = f"{BASE_URL}/products/{created_product['id']}"
    payload = {
        "name": "Wireless Mouse",
        "price": 2500
    }
    response = requests.put(url, json=payload, timeout=10)
    assert response.status_code == 200
    data = response.json()
    validate(data, product_schema)
    assert data['name'] == payload['name']
    assert data['price'] == payload['price']
    assert data['id'] == created_product['id']

    response_get = requests.get(url, timeout=10)
    assert response_get.status_code == 200
    data_get = response_get.json()
    validate(data_get, product_schema)
    assert data_get['name'] == payload['name']
    assert data_get['price'] == payload['price']
    assert data_get['id'] == created_product['id']

def test_update_nonexistent_product():
    product_id = 999999
    url = f"{BASE_URL}/products/{product_id}"
    payload = {
        "name": "Wireless Mouse",
        "price": 2500
    }
        
    response = requests.put(url, json=payload, timeout=10)
    assert response.status_code == 404
    data = response.json()
    assert isinstance(data, dict)
    assert "Product not found" in data['detail']
    response_get = requests.get(url, timeout=10)
    assert response_get.status_code == 404  
    
def test_create_product():
    payload = {
        "name": "Keyboard",
        "price": 3500
    }
    url = f"{BASE_URL}/products"
    product_id = None
    try:
        response = requests.post(url, json=payload, timeout=10)
        assert response.status_code == 201
        data = response.json()

        # Keep the ID checks before validation so the finally block can clean up.
        assert isinstance(data, dict)
        assert isinstance(data['id'], int)
        assert data['id'] > 0
        product_id = data['id']

        validate(data, product_schema)
        assert data['name'] == payload['name']
        assert data['price'] == payload['price']

        response_get= requests.get(f'{url}/{product_id}', timeout=10)
        assert response_get.status_code == 200
        data_get = response_get.json()
        validate(data_get, product_schema)
        assert data_get['name'] == payload['name']
        assert data_get['price'] == payload['price']
        assert data_get['id'] == product_id

    finally:
        if product_id is not None:
            response_del = requests.delete(f'{url}/{product_id}', timeout=10)
            assert response_del.status_code == 200
            response_get = requests.get(f"{BASE_URL}/products/{data['id']}",
                    timeout=10)
            assert response_get.status_code == 404
            data_get = response_get.json()
            assert isinstance(data_get, dict)
            assert "Product not found" in data_get['detail']
            
def test_create_product_without_price():
    payload = {
        "name": "Keyboard"
    }
    url = f"{BASE_URL}/products"
    response = requests.post(url, json=payload, timeout=10)
    assert response.status_code == 422
    data = response.json()
    assert isinstance(data, dict)
    assert isinstance(data['detail'], list)
    assert len(data['detail']) == 1
    assert isinstance(data['detail'][0], dict)
    error =  data['detail'][0]
    assert error['type'] == 'missing'
    assert error['loc'] == ["body", "price"]
    assert error['msg'] == "Field required"
    

def test_delete_product():
    payload = {
        "name": "Monitor",
        "price": 15000
    }
    url = f"{BASE_URL}/products"
    product_id = None
    try:
        response_post = requests.post(url, json=payload, timeout=10)
        assert response_post.status_code == 201
        data = response_post.json()

        # Keep the ID checks before validation so the finally block can clean up.
        assert isinstance(data, dict)
        assert isinstance(data['id'], int)
        assert data['id'] > 0
        product_id = data['id']
        validate(data, product_schema)

        product_url = f'{BASE_URL}/products/{data['id']}'
        
        response_get = requests.get(product_url, timeout=10)
        assert response_get.status_code == 200
        
        response_del = requests.delete(product_url, timeout=10)
        assert response_del.status_code == 200
        data_del = response_del.json()
        validate(data_del, message_schema)
        assert data_del['message'] == "Product deleted"
        
        response_get = requests.get(product_url,
                timeout=10)
        assert response_get.status_code == 404
        data_get = response_get.json()
        assert isinstance(data_get, dict)
        assert "Product not found" in data_get['detail']

    finally:
        if product_id is not None:
            final_response = requests.get(product_url, timeout=10)
            assert final_response.status_code in (200, 404)
            if final_response.status_code == 200:
                response_delite = requests.delete(product_url, timeout=10)
                assert response_delite.status_code == 200
                data_delite = response_delite.json()
                validate(data_delite, message_schema)
                assert data_delite['message'] == "Product deleted"
                
                response_get = requests.get(product_url,
                        timeout=10)
                assert response_get.status_code == 404
                data_get = response_get.json()
                assert isinstance(data_get, dict)
                assert data_get['detail'] == "Product not found"
               
def test_get_nonexistent_product():
    payload = {
        "name": "Headphones",
        "price": 4500
    }
    product_id = None
    try:
        responae_post = requests.post(f"{BASE_URL}/products", json=payload, timeout=10)
        assert responae_post.status_code == 201
        data_post = responae_post.json()
        assert isinstance(data_post, dict)
        assert type(data_post['id']) is int
        assert data_post['id'] > 0
        
        product_id = data_post['id']
        product_url = f"{BASE_URL}/products/{product_id}"
        
        response = requests.get(product_url, timeout=10)
        assert response.status_code == 200
        
        response_del = requests.delete(product_url, timeout=10)
        assert response_del.status_code == 200
        data_del = response_del.json()
        assert isinstance(data_del, dict)
        assert isinstance(data_del['message'], str)
        assert data_del['message'] == "Product deleted"
        
        response_get = requests.get(product_url, timeout=10)
        assert response_get.status_code == 404
        data_get = response_get.json()
        assert isinstance(data_get, dict)
        assert data_get['detail'] == "Product not found"
    
    finally:
            if product_id is not None:
                final_response = requests.get(product_url, timeout=10)
                assert final_response.status_code in (200, 404)
                if final_response.status_code == 200:
                    response_delite = requests.delete(product_url, timeout=10)
                    assert response_delite.status_code == 200
                    data_delite = response_delite.json()
                    assert isinstance(data_delite, dict)
                    assert isinstance(data_delite['message'], str)
                    assert data_delite['message'] == "Product deleted"
                    
                    response_get = requests.get(product_url,
                            timeout=10)
                    assert response_get.status_code == 404
                    data_get = response_get.json()
                    assert isinstance(data_get, dict)
                    assert data_get['detail'] == "Product not found"
    
def test_delete_nonexistent_product():
    payload = {
        "name": "Webcam",
        "price": 5000
    }
    product_id = None
    
    try:
        response_post = requests.post(f"{BASE_URL}/products", json=payload, timeout=10)
        assert response_post.status_code == 201
        data_post = response_post.json()
        assert isinstance(data_post, dict)
        assert type(data_post['id']) is int
        assert data_post['id'] > 0
        
        product_id = data_post['id']
        product_url = f"{BASE_URL}/products/{product_id}"
        
        response_del = requests.delete(product_url, timeout=10)
        assert response_del.status_code == 200
        data_del = response_del.json()
        assert isinstance(data_del, dict)
        assert isinstance(data_del['message'], str)
        assert data_del['message'] == "Product deleted"
        
        response_get = requests.get(product_url, timeout=10)
        assert response_get.status_code == 404
        data_get = response_get.json()
        assert isinstance(data_get, dict)
        assert data_get['detail'] == "Product not found"

        response_del_nonexistent = requests.delete(product_url, timeout=10)
        assert response_del_nonexistent.status_code == 404
        data_del_nonexistent = response_del_nonexistent.json()
        assert isinstance(data_del_nonexistent, dict)
        assert data_del_nonexistent['detail'] == "Product not found"
        
        response_get_after_del = requests.get(product_url, timeout=10)
        assert response_get_after_del.status_code == 404
        data_get_after_del = response_get_after_del.json()  
        assert isinstance(data_get_after_del, dict)
        assert data_get_after_del['detail'] == "Product not found"
    
    finally:
        if product_id is not None:
            final_response = requests.get(product_url, timeout=10)
            assert final_response.status_code in (200, 404)
            if final_response.status_code == 200:
                response_delite = requests.delete(product_url, timeout=10)
                assert response_delite.status_code == 200
                data_delite = response_delite.json()
                assert isinstance(data_delite, dict)
                assert isinstance(data_delite['message'], str)
                assert data_delite['message'] == "Product deleted"
                
                response_get = requests.get(product_url,
                        timeout=10)
                assert response_get.status_code == 404
                data_get = response_get.json()
                assert isinstance(data_get, dict)
                assert data_get['detail'] == "Product not found"
             
        
    