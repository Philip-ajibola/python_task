from unittest import TestCase

from account import Account
from account_does_not_exist_exception import AccountNotFoundException
from bank import Bank
from invalid_pin_exception import InvalidPinException


class TestBank(TestCase):
    def setUp(self):
        self.bank = Bank("Ajibola's Bank")

    def test_that_I_can_register_Account(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        self.assertEqual(1, self.bank.number_of_customers())

    def test_that_I_can_register_more_customer(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        self.assertEqual(2, self.bank.number_of_customers())

    def test_that_account_can_be_found(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        account2 = self.bank.find_account(1)
        with self.assertRaises(AccountNotFoundException):
            account3 = self.bank.find_account(3)
        self.assertEqual(account, account2)

    def test_that_when_I_find_account_that_does_exist_error_message_is_thrown(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        with self.assertRaises(AccountNotFoundException):
            account2 = self.bank.find_account(3)

    def test_that_I_can_remove_account_from_bank(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        self.bank.remove_account(account, "pin")
        self.assertEqual(1, self.bank.get_number_of_active_account())

    def test_when_I_try_to_remove_account_with_wrong_pin_error_message_is_thrown(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        self.bank.remove_account(account, "pin")
        self.assertEqual(1, self.bank.get_number_of_active_account())
        with self.assertRaises(InvalidPinException):
            self.bank.remove_account(account1, "not_pin")

    def test_when_I_try_to_remove_an_account_that_not_exist_error_message_is_thrown(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        account2 = Account("firstName", 4, "pin")
        self.bank.remove_account(account, "pin")
        self.assertEqual(1, self.bank.get_number_of_active_account())
        with self.assertRaises(AccountNotFoundException):
            self.bank.remove_account(account2, "pin")

    def test_that_when_i_remove_account_and_try_to_find_it_error_message_is_thrown(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        self.bank.remove_account(account, "pin")
        with self.assertRaises(AccountNotFoundException):
            self.bank.remove_account(account, "pin")
        self.assertEqual(1, self.bank.get_number_of_active_account())

    def test_that_money_can_be_deposited(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        self.bank.deposit(1, 2_000)
        self.assertEqual(2_000, self.bank.check_balance(1, "pin"))

    def test_that_I_cant_check_balance_when_pin_wrong(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        self.bank.deposit(1, 2_000)
        with self.assertRaises(InvalidPinException):
            self.bank.check_balance(1, "wrong_pin")

    def test_that_I_can_withdraw_from_bank(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        self.bank.deposit(1, 2_000)
        self.bank.withdraw(1, 1_000, "pin")
        self.assertEqual(1_000, self.bank.check_balance(1, "pin"))

    def test_that_when_pin_is_wrong_money_cant_be_withdrawn(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        self.bank.deposit(1, 2_000)
        with self.assertRaises(InvalidPinException):
            self.bank.withdraw(1, 1_000, "wrong_pin")
        self.assertEqual(2_000, self.bank.check_balance(1, "pin"))

    def test_that_when_multiple_account_is_created_different_account_number_is_generated(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        account2 = self.bank.register_customer("firstName", "lastName", "pin")
        self.assertEqual(1, account.get_number())
        self.assertEqual(2, account1.get_number())
        self.assertEqual(3, account2.get_number())

    def test_that_when_one_account_is_removed_and_new_one_is_add_the_account_number_is_different(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        account2 = self.bank.register_customer("firstName", "lastName", "pin")

        self.assertEqual(1, account.get_number())
        self.assertEqual(2, account1.get_number())
        self.bank.remove_account(account, "pin")
        self.assertEqual(3, account2.get_number())
        account3 = self.bank.register_customer("firstName", "lastName", "pin")
        self.assertEqual(4, account3.get_number())

    def test_that_i_can_transfer_from_one_account_to_another_account(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        self.bank.deposit(1, 5_000)
        self.bank.transfer(1, 2, 3_000, "pin")
        self.assertEqual(3_000, self.bank.check_balance(2, "pin"))

    def test_that_i_want_transfer_with_wrong_pin_error_should_be_thrown(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        self.bank.deposit(1, 5_000)
        with self.assertRaises(InvalidPinException):
            self.bank.transfer(1, 2, 3_000, "wrong_pin")
        self.assertEqual(0, self.bank.check_balance(2, "pin"))

    def test_that_negative_amount_cant_be_transferred(self):
        account = self.bank.register_customer("firstName", "lastName", "pin")
        account1 = self.bank.register_customer("firstName", "lastName", "pin")
        self.bank.deposit(1, 5_000)
        with self.assertRaises(InvalidPinException):
            self.bank.transfer(1, 2, 3_000, "wrong_pin")
        self.assertEqual(0, self.bank.check_balance(2, "pin"))
