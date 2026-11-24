import requests


def test_create_post():
    url = 'https://jsonplaceholder.typicode.com/posts'
    payload = {
    "title": "Learning QA Automation",
    "body": "My first CRUD API suite",
    "userId": 5
    }
    response = requests.post(url, json=payload, timeout=10)
    assert response.status_code == 201
    data = response.json()
    assert isinstance(data, dict)
    assert data['title'] == payload['title']
    assert data['body'] == payload['body']
    assert data['userId'] == payload['userId']
    assert 'id' in data
    assert isinstance(data['id'], int)
    assert data['id'] >0

def test_get_post():
    url = 'https://jsonplaceholder.typicode.com/posts/10'
    response = requests.get(url, timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert 'id' in data
    assert data['id'] == 10
    assert isinstance(data['userId'], int)
    assert data['userId'] > 0
    assert isinstance(data['title'], str)
    assert data['title'].strip()
    assert isinstance(data['body'], str)
    assert data['body'].strip()

def test_update_post():
    url = 'https://jsonplaceholder.typicode.com/posts/10'
    payload = {
        "id": 10,
        "title": "Updated QA Automation",
        "body": "Learning PUT requests",
        "userId": 2
        }
    response = requests.put(url, json=payload, timeout=10)
    assert response.status_code == 200
    data = response.json()
    
    assert data['id'] == payload['id']
    assert isinstance(data['title'], str)
    assert data['title'] == payload['title']
    assert isinstance(data['body'], str)
    assert data['body'] == payload['body']
    assert isinstance(data['userId'], int)
    assert data['userId'] == payload['userId']
    # response_changed = requests.get(url, timeout=10)
    # data_changed = response_changed.json()
    # assert payload['title'] == data_changed['title']

def test_delete_post():
    url = 'https://jsonplaceholder.typicode.com/posts/10'
    response = requests.delete(url, timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data == {}