import pytest

@pytest.fixture
def user_data():
    return {
        "id": 101,
        "username": "tester",
        "email": "tester@example.com",
        "active": True,
        "roles": ["user", "editor"]
    }


def test_username(user_data):
    assert user_data['username'] == 'tester'


def test_user_active(user_data):
    assert user_data['active'] is True
    

def test_user_role(user_data):
    assert 'editor' in user_data['roles']


def test_change_username(user_data):
    user_data['username'] = 'admin'
    assert user_data['username'] == 'admin'
    

def test_original_username(user_data):
    assert user_data['username'] == 'tester'
    
    
    