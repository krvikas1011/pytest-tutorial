import pytest
from e_Wallet_Application.src.wallet import Wallet, InsufficientAmount


def setup_module(module):
    print("Before")
    """ setup any state specific to the execution of the given module."""


def teardown_module(module):
    print("After")
    """ teardown any state that was previously setup with a setup_module
    method."""


@pytest.fixture
def empty_wallet():
    """Returns a wallet instance with 0 balance"""
    return Wallet()


@pytest.fixture
def money_wallet():
    """Returns a wallet instance with 20 balance"""
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(money_wallet):
    assert money_wallet.balance == 20


def test_wallet_add_cash(money_wallet):
    money_wallet.add_cash(80)
    assert money_wallet.balance == 100


def test_wallet_spend_cash(money_wallet):
    """This showcases that a new instance of money_wallet is passed in each test."""
    money_wallet.spend_cash(10)
    assert money_wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(10)
