import requests
import pytest

class APIClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.session = requests.Session()
    
    def get_post(self, post_id):
        response = self.session.get(f'{self.base_url}/posts/{post_id}', timeout=10)
        
        return response
    
    def create_post(self, payload):
        response = self.session.post(f'{self.base_url}/posts', json = payload, timeout=10)
        
        return response

    def close(self):
        self.session.close()
    
@pytest.fixture
def api_client():
    api_client = APIClient()
    yield api_client
    api_client.close()

def test_get_post_3(api_client):
    response = api_client.get_post(3)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 3
    assert data['userId'] == 1
    
def test_get_post_8(api_client):
    response = api_client.get_post(8)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 8
    assert data['userId'] == 1

def test_create_post(api_client):
    payload = {
    "title": "Learning API Automation",
    "body": "Pytest fixtures and API Client",
    "userId": 1
}
    response = api_client.create_post(payload)
    assert response.status_code == 201
    data = response.json()
    
    assert data['title'] == payload['title']
    assert data['body'] == payload['body']
    assert data['userId'] == payload['userId']
    assert 'id' in data
    