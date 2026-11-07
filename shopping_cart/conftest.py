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


@pytest.fixture
def cart_with_cleanup():
    print('SETUP: creating cart')
    cart = ShoppingCart()
    yield cart
    cart.clear()
    print('TEARDOWN: cart cleared')
    
@pytest.fixture
def prepared_cart_with_cleanup():
    cart = ShoppingCart()
    cart.add_item('keyboard', 2000, 2)
    print('SETUP: prepared cart')
    yield cart
    cart.clear()
    print('TEARDOWN: prepared cart cleared')

