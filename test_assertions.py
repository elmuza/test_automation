user_response = {
    "status_code": 200,
    "body": {
        "id": 101,
        "username": "tester",
        "email": "tester@example.com",
        "active": True,
        "roles": ["user", "editor"]
    },
    "duration": 0.35
}

login_response = {
    "status_code": 401,
    "body": {
        "error": "Invalid credentials",
        "authenticated": False,
        "token": None
    },
    "duration": 0.28
}

def test_user_response_positive():
    assert user_response['status_code'] == 200
    assert user_response['body']['id'] == 101
    assert user_response['body']['username'] == 'tester', 'Имя пользователя не tester'
    assert 'email' in user_response['body']
    assert 'editor' in user_response['body']['roles']
    assert user_response['duration'] < 1, 'Время ответа больше 1 секунды'


def test_login_wrong_password():
    assert login_response['status_code'] == 401
    assert 'error' in login_response['body'], 'Ключа error не существует'
    assert login_response['body']['error'] == 'Invalid credentials'
    assert login_response['body']['authenticated'] is False
    assert login_response['body']['token'] is None, 'Значение токена отлично от None'


