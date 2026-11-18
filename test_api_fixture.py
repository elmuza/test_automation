import pytest
import requests


url = 'https://jsonplaceholder.typicode.com'
@pytest.fixture
def api_session():
    with requests.Session() as session:
        yield session
    
def test_get_post_5(api_session):
    response = api_session.get(url+'/posts/5', timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 5

def test_get_post_6(api_session):
    response = api_session.get(url+'/posts/6', timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 6
    