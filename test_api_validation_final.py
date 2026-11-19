import requests


url ='https://jsonplaceholder.typicode.com/'


def test_user_validation():
    response = requests.get(f'{url}users/3', timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data['id'] == 3
    assert isinstance(data['username'], str)
    assert data['username'].strip()
    assert 'email' in data
    assert '@' in data['email']

def test_post_validation():
    response = requests.get(f'{url}posts/15', timeout=10)
    assert response.status_code == 200
    headers = response.headers
    assert 'Content-type' in headers
    assert 'application/json' in headers['Content-type']
    data = response.json()
    assert data['id'] == 15
    assert isinstance(data['userId'], int)
    assert isinstance(data['title'], str)
    assert data['title'].strip()

def test_post_not_found():
    response = requests.get(f'{url}posts/999999', timeout=10)
    assert response.status_code == 404
    data = response.json()
    assert isinstance(data, dict)
    assert data == {}

def test_post_business_validation():
    response = requests.get(f'{url}posts/20', timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data['id'], int)
    assert data['id'] > 0
    assert isinstance(data['userId'], int)
    assert data['userId'] > 0
    assert isinstance(data['title'], str)
    assert data['title'].strip()
    assert isinstance(data['body'], str)
    assert data['body'].strip()