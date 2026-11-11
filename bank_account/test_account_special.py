import pytest
import sys

@pytest.mark.skip("Функция заморозки счёта пока не реализована")
def test_frozen_account(account):
    pass


@pytest.mark.skipif(sys.platform !='win32', reason="Test works only on Windows")
def test_windows_only():
    assert sys.platform == 'win32'
    
@pytest.mark.xfail
def test_known_bug(account):
    assert account.balance == 2000
    
def test_negative_deposit(account):
     with pytest.raises(ValueError):
        account.deposit(-100)
