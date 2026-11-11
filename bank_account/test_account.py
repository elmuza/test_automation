from account import BankAccount
import pytest

@pytest.mark.smoke
def test_create_account():
    account = BankAccount('Anna', 1000)
    assert account.owner == 'Anna'
    assert account.balance == 1000

@pytest.mark.smoke
def test_default_balance():
    account = BankAccount('Anna')
    assert account.balance == 0
 
@pytest.mark.regression    
def test_deposit():
    account = BankAccount('Anna', 1000)
    account.deposit(500)
    assert account.balance == 1500

@pytest.mark.regression    
def test_withdraw():
    account = BankAccount('Anna', 1000)
    account.withdraw(300)
    assert account.balance == 700
    
@pytest.mark.regression
def test_get_balance():
    account = BankAccount('Anna', 1000)
    assert account.get_balance() == 1000

@pytest.mark.regression
@pytest.mark.smoke
def test_transfer():
    account_base = BankAccount('Anna', 1000)
    account_target = BankAccount('Bob', 500)
    
    account_base.transfer(account_target, 400)
    
    assert account_base.balance == 600
    assert account_target.balance == 900

def test_deposit_with_fixture(account):
    account.deposit(200)
    assert account.balance == 1200

def test_withdraw_with_fixture(account):
    account.withdraw(400)
    assert account.balance == 600
    
def test_account_with_cleanup(account_with_cleanup):
    assert account_with_cleanup.balance == 2000
    account_with_cleanup.deposit(500)
    assert account_with_cleanup.balance == 2500
    