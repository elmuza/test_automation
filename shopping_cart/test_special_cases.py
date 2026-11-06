import pytest


import sys


@pytest.mark.skip(reason="Discount feature is not implemented")
def test_discount(cart):
    cart.add_item("mouse", 1000)
    cart.apply_discount(10)
    assert cart.get_total() == 900
    
    
@pytest.mark.skipif(sys.platform == "win32", reason="Test works only on Linux")
def test_linux_only():
    assert sys.platform == "linux"
    

@pytest.mark.xfail(reason="BUG-101: discount is not implemented") 
def test_discount_bug(cart):
    cart.add_item("mouse", 1000)
    cart.apply_discount(10)
    assert cart.get_total() == 900
    
    
