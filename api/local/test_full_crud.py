import requests
import pytest


BASE_URL = "http://localhost:8000"

@pytest.fixture
def created_product():
    payload = {
    "name": "Mouse",
    "price": 1500
    }
    response = requests.post(f"{BASE_URL}/products", json=payload, timeout=10)
    assert response.status_code == 201
    data = response.json()
    assert isinstance(data, dict)
    yield data
    response =requests.delete(f"{BASE_URL}/products/{data['id']}", timeout=10)
    assert response.status_code == 200

def test_get_created_product(created_product):
    url = f"{BASE_URL}/products/{created_product['id']}"
    response = requests.get(url, timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data['id'] == created_product['id']
    assert data['name'] == created_product['name']
    assert data['price'] == created_product['price']
