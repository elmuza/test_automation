import requests


def test_get_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users/3', timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 3
    assert data["username"] == "Samantha"
    
       