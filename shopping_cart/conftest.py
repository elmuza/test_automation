import pytest

from cart import ShoppingCart


@pytest.fixture(scope="function")
def cart():
    return ShoppingCart()