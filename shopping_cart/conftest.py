import pytest


from cart import ShoppingCart


@pytest.fixture(scope="function")
def cart():
    return ShoppingCart()


@pytest.fixture
def prepared_cart(request):
    cart = ShoppingCart()

    quantity = request.param

    cart.add_item("mouse", 500, quantity)

    return cart


@pytest.fixture
def configured_cart(request):
    cart = ShoppingCart()
    data = request.param
    name = data["name"]
    price = data["price"]
    quantity = data["quantity"]
    cart.add_item(name, price, quantity)
    return cart
    