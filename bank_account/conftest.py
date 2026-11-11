import pytest
from account import BankAccount

@pytest.fixture(scope='function')
def account():
    account = BankAccount('Anna', 1000)
    return account

@pytest.fixture()
def account_with_cleanup():
    account = BankAccount('Bob', 2000)
    print('SETUP: account created')
    yield account
    account.balance = 0
    print('TEARDOWN: account cleared')

@pytest.fixture()
def configured_account(request):
    data = request.param
    owner = data['owner']
    balance = data['balance']
    account = BankAccount(owner, balance)
    return account


    