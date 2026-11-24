import requests
import pytest

class APIClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.session = requests.Session()
        
    def get_user(self, user_id):
        request = self.session.get(self.base_url+'/users/'+str(user_id), timeout=10)
        return request
    
    def close(self):
        self.session.close()
    

@pytest.fixture
def api_client():
    api_client = APIClient()
    yield api_client
    api_client.close
    
    
def test_get_user_1(api_client):
    request = api_client.get_user(1)
    assert request.status_code == 200
    data = request.json()
    assert data['id'] == 1
    assert data['username'] == 'Bret'

def test_get_user_2(api_client):
    request = api_client.get_user(2)
    assert request.status_code == 200
    data = request.json()
    assert data['id'] == 2
    assert data['username'] == 'Antonette'

