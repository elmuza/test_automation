def login(username, password):
    if username == "admin" and password == "password":
        return True

    return False

def test_login_success():
    assert login("admin", "password") is True

def test_login_wrong_password():
    assert login("admin", "wrong_password") is False
    
