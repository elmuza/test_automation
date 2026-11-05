import pytest


@pytest.fixture(scope="module")
def database_connection():
    print("\nСоздаём подключение к базе данных")
    return {"connected": True}


def test_connection_one(database_connection):
    assert database_connection['connected'] is True
    
    
def test_connection_two(database_connection):
    assert database_connection['connected'] is True
    
    
def test_connection_three(database_connection):
    assert database_connection['connected'] is True
