from unittest import TestCase

from account import Account
from insufficient_funds_exception import InsufficientFundsException
from invalid_amount_exception import InvalidAmountException
from invalid_pin_exception import InvalidPinException


class TestAccount(TestCase):
    def test_that_balance_is_zero_at_point_of_creation(self):
        account = Account("firstName LastName", 1, "correct_pin")
        self.assertEqual(0, account.check_balance("correct_pin"))

    def test_that_I_can_deposit(self):
        account = Account("firstName LastName", 1, "correct_pin")
        account.deposit(500)
        self.assertEqual(500, account.check_balance("correct_pin"))

    def test_that_I_can_deposit_multiple_times(self):
        account = Account("firstName LastName", 1, "correct_pin")
        account.deposit(500)
        account.deposit(2_500)
        self.assertEqual(3_000, account.check_balance("correct_pin"))

    def test_that_I_cant_deposit_negative_number(self):
        account = Account("firstName LastName", 1, "correct_pin")
        with self.assertRaises(InvalidAmountException):
            account.deposit(-500)

    def test_that_when_pin_is_wrong_exception_thrown(self):
        account = Account("firstName LastName", 1, "correct_pin")
        account.deposit(500)
        with self.assertRaises(InvalidPinException):
            account.check_balance("wrong_pin")

    def test_that_I_can_withdraw_money_from_account(self):
        account = Account("firstName LastName", 1, "correct_pin")
        account.deposit(5_000)
        account.withdraw(1_000, "correct_pin")
        self.assertEqual(4_000, account.check_balance("correct_pin"))

    def test_that_I_can_withdraw_money_from_account_multiple_times(self):
        account = Account("firstName LastName", 1, "correct_pin")
        account.deposit(5_000)
        account.withdraw(1_000, "correct_pin")
        account.withdraw(2_000, "correct_pin")
        self.assertEqual(2_000, account.check_balance("correct_pin"))

    def test_that_I_cant_withdraw_negative_amount_from_account(self):
        account = Account("firstName LastName", 1, "correct_pin")
        account.deposit(5_000)
        with self.assertRaises(InvalidAmountException):
            account.withdraw(-1_000, "correct_pin")
        self.assertEqual(5_000, account.check_balance("correct_pin"))

    def test_that_I_cant_withdraw_amount_greater_than_balance_from_account(self):
        account = Account("firstName LastName", 1, "correct_pin")
        account.deposit(5_000)
        with self.assertRaises(InsufficientFundsException):
            account.withdraw(6_000, "correct_pin")
        self.assertEqual(5_000, account.check_balance("correct_pin"))

    def test_that_I_cant_withdraw_when_pin_is_wrong(self):
        account = Account("firstName LastName", 1, "correct_pin")
        account.deposit(5_000)
        with self.assertRaises(InvalidPinException):
            account.withdraw(3_000, "wrong_pin")
