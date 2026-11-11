import pytest

@pytest.mark.parametrize('amount, expected_balance', [
        (100, 1100),
        (500, 1500),
        (1000, 2000),
        (2500, 3500),
    ])
def test_deposit_parametrize(account, amount, expected_balance):
    account.deposit(amount)
    assert account.balance == expected_balance

@pytest.mark.parametrize('configured_account, owner, balance',[
        pytest.param({'owner': 'Anna', 'balance': 1000}, 'Anna', 1000),
        pytest.param({'owner': 'Bob', 'balance': 2000}, 'Bob', 2000),
        pytest.param({'owner': 'Charlie', 'balance': 500}, 'Charlie', 500),
    ], indirect=['configured_account'])
def test_configured_account(configured_account, owner, balance):
    assert configured_account.owner == owner
    assert configured_account.balance == balance
