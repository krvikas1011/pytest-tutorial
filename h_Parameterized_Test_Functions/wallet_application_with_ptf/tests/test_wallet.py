import pytest
from e_Wallet_Application.src.wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    """Returns a wallet instance with 0 balance"""
    return Wallet()


@pytest.fixture
def money_wallet():
    """Returns a wallet instance with 20 balance"""
    return Wallet(20)


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
    (200, 20, 180),
    (120, 2, 118),
    (20, 20, 0)
])
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions_empty_wallet(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 40),
    (20, 2, 38),
])
def test_transactions_money_wallet(money_wallet, earned, spent, expected):
    money_wallet.add_cash(earned)
    money_wallet.spend_cash(spent)
    assert money_wallet.balance == expected
