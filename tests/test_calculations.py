
import pytest
from app.calculations import *

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    print ("Testing add function")
    assert add(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 1),
    (7, 1, 6),
    (12, 4, 8)
])
def test_subtract(num1, num2, expected):
    print ("Testing subtract function")
    assert subtract(num1, num2) == expected


def test_multiply():
    print ("Testing multiply function")
    assert multipy(2, 4) == 8

def test_divide():
    print ("Testing divide function")
    assert divide(24, 3) == 8


def test_bank_set_initial_amount(bank_account):
    # bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    # bank_account = BankAccount()
    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):
    # bank_account = BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_deposit(bank_account):
    # bank_account = BankAccount(50)
    bank_account.deposit(20)
    assert bank_account.balance == 70


def test_collect_interest(bank_account):
    # bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance, 2) == 55

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (300, 25, 275),
    (1000, 250, 750),
    (1250, 400, 850)
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)