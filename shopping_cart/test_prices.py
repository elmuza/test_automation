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
