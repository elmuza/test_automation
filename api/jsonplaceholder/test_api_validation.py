import pytest
import requests

def test_user_body():
    url = 'https://jsonplaceholder.typicode.com/users/5'
    with requests.Session() as session:
        response = session.get(url, timeout=10)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert data['id'] == 5
        assert 'username' in data
        assert isinstance(data['username'], str)
        assert len(data['username'])>0
        assert 'email' in data
        assert type(data['email']) is str
        assert '@' in data['email']
        
def test_post_headers():
    url = 'https://jsonplaceholder.typicode.com/posts/7'
    response = requests.get(url, timeout=10)
    assert response.status_code == 200
    header = response.headers
    assert 'Content-Type' in header
    content_type = header['Content-Type']
    assert 'application/json' in content_type
    data = response.json()
    assert data['id']  == 7
    
def test_user_not_found():
    url = 'https://jsonplaceholder.typicode.com/users/999999'
    response = requests.get(url, timeout=10)
    assert response.status_code == 404
    data =response.json()
    assert isinstance(data, dict)
    assert data == {}

def test_post_business_rules():
    url = 'https://jsonplaceholder.typicode.com/posts/12'
    response = requests.get(url, timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data['id'], int)
    assert data['id'] > 0
    assert isinstance(data['userId'], int)
    assert data['userId'] > 0
    assert isinstance(data['title'], str)
    assert len(data['title'].strip()) > 0
    assert isinstance(data['body'], str)
    assert len(data['body'].strip()) > 0