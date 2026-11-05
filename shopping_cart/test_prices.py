import pytest


def test_single_item_price(cart):
    cart.add_item('mouse', 700)
    assert cart.get_total() == 700
    assert cart.get_item_count() == 1


def test_multiple_items_price(cart):
    cart.add_item('keyboard', 1200, 3)
    assert cart.get_total() == 3600
    assert cart.get_item_count() == 3
    assert len(cart.items) == 1


@pytest.mark.parametrize(
    'price, quantity, expected_total',
    [
        (100, 1, 100),
        (250, 2, 500),
        (400, 3, 1200),
        (1000, 5, 5000),
    ]
)
def test_product_total(cart, price, quantity, expected_total):
    cart.add_item('mouse', price, quantity)
    assert cart.get_total() == expected_total
    
    
@pytest.mark.parametrize(
    "prepared_cart",
    [1, 2, 5],
    indirect=True
)
def test_prepared_cart(prepared_cart):
    assert prepared_cart.get_total() == prepared_cart.get_item_count()*500
    

@pytest.mark.parametrize("configured_cart, expected_total", [
    pytest.param({"name": "mouse", "price": 500, "quantity": 2}, 1000, id='mouse'), 
    pytest.param({"name": "keyboard", "price": 1500, "quantity": 1}, 1500, id='keyboard'), 
    pytest.param({"name": "monitor", "price": 10000, "quantity": 2}, 20000, id='monitor')], indirect=["configured_cart"] )
def test_configured_cart(configured_cart, expected_total):
    assert configured_cart.get_total() == expected_total
    assert len(configured_cart.items) == 1
    