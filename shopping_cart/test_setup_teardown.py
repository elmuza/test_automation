
def test_cart_cleanup(cart_with_cleanup):
    cart_with_cleanup.add_item('mouse', 500, 2)
    assert cart_with_cleanup.get_total() == 1000
    assert cart_with_cleanup.get_item_count() == 2


def test_cleanup_after_failure(cart_with_cleanup):
    cart_with_cleanup.add_item('keyboard', 1500)
    assert cart_with_cleanup.get_total() == 1500
    