def test_single_item_price(cart):
    cart.add_item('mouse', 700)
    assert cart.get_total() == 700
    assert cart.get_item_count() == 1


def test_multiple_items_price(cart):
    cart.add_item('keyboard', 1200, 3)
    assert cart.get_total() == 3600
    assert cart.get_item_count() == 3
    assert len(cart.items) == 1
        