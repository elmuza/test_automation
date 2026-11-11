def test_bank_account_fixture(account):
    assert account.owner == 'Anna'
    assert account.balance == 1000

def test_deposit_fixture(account):
    account.deposit(700)
    assert account.balance == 1700

def test_account_cleanup(account_with_cleanup):
    assert account_with_cleanup.balance == 2000
    account_with_cleanup.withdraw(500)
    assert account_with_cleanup.balance == 1500
