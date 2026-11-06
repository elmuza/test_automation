import pytest


import sys


@pytest.mark.skip(reason='Оплата ещё не реализована')
def test_payment(cart):
    cart.add_item("mouse", 1000)
    assert cart.get_total() == 1000
    assert cart.pay() == cart.get_total()
   
   
@pytest.mark.skipif(sys.platform == 'win32', reason='Пропускать только на Windows')
def test_linux_payment():
    assert sys.platform == 'linux'


@pytest.mark.xfail(reason='Равенство неверное')
def test_known_bug():
    assert 2+2 == 5


