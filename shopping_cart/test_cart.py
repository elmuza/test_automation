import pytest


def test_empty_cart(cart):
    assert cart.get_item_count() == 0
    assert cart.get_total() == 0
    assert cart.items == []
    

def test_add_items(cart):
    cart.add_item('mouse', 500, 2)
    cart.add_item('keyboard', 1500)
    
    assert cart.get_item_count() == 3
    assert cart.get_total() == 2500
    assert len(cart.items) == 2
    
    
def test_remove_item(cart):
    cart.add_item('mouse', 500, 2)
    cart.add_item('keyboard', 1500)
    result = cart.remove_item("mouse")
    
    assert result is True
    assert cart.items[0]['name'] == 'keyboard'
    assert cart.get_item_count() == 1
    assert cart.get_total() == 1500
    assert len(cart.items) == 1
    

def test_clear_cart(cart):
    cart.add_item('mouse', 500, 2)
    cart.add_item('keyboard', 1500)
    cart.clear()
    
    assert len(cart.items) == 0
    assert cart.get_item_count() == 0
    assert cart.get_total() == 0


def test_negative_price(cart):
    with pytest.raises(ValueError):
        cart.add_item('mouse', -500)
    
    assert len(cart.items) == 0


def test_zero_quantity(cart):
    with pytest.raises(ValueError):
        cart.add_item('mouse', 500, 0)
    
    assert len(cart.items) == 0
    