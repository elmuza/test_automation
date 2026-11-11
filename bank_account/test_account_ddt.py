import json
from pathlib import Path
import csv
import pytest
from bank_account.account import BankAccount


path_json = Path(__file__).parent / 'deposits.json'
with path_json.open('r', encoding='utf-8') as file:
    accounts = json.load(file)

account_data = [
    (
        item['owner'],
        item['initial_balance'],
        item['deposit'],
        item['expected_balance'],
    )
    for item in accounts
]


@pytest.mark.parametrize(
    'owner, initial_balance, deposit, expected_balance',
    account_data,
    ids=[item['owner'] for item in accounts],
)
def test_deposit_from_json(owner, initial_balance, deposit, expected_balance):
    account = BankAccount(owner, initial_balance)
    account.deposit(deposit)
    assert account.balance == expected_balance

path_csv = Path(__file__).parent / 'withdrawals.csv'
with path_csv.open('r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    withdrawal_data = [
        (
            row['owner'],
            float(row['initial_balance']),
            float(row['withdraw']),
            float(row['expected_balance']),
        )
        for row in reader
    ]

@pytest.mark.parametrize(
    'owner, initial_balance, withdraw, expected_balance',
    withdrawal_data,
    ids=[item[0] for item in withdrawal_data],
)
def test_withdrawal_from_csv(owner, initial_balance, withdraw, expected_balance):
    account = BankAccount(owner, initial_balance)
    account.withdraw(withdraw)
    assert account.balance == expected_balance
