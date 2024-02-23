from decimal import Decimal

from insufficient_funds_exception import InsufficientFundsException
from invalid_amount_exception import InvalidAmountException
from invalid_pin_exception import InvalidPinException


class Account:
    def __init__(self, account_name, account_number, account_pin):
        self.account_name = account_name
        self.__balance = 0
        self.__account_number = account_number
        self.__account_pin = account_pin

    def deposit(self, amount: int) -> None:
        if self.__is_amount_valid(amount): raise InvalidAmountException("Invalid Amount")
        self.__balance += amount

    def check_balance(self, pin: str) -> int:
        if self.is_pin_not_valid(pin): raise InvalidPinException("Invalid Pin")
        return self.__balance

    def withdraw(self, amount: int, pin) -> None:
        if self.is_pin_not_valid(pin): raise InvalidAmountException("Invalid Amount")
        if self.__is_amount_valid(amount): raise InvalidAmountException("Invalid Amount")
        if self.__is_balance_insufficient(amount): raise InsufficientFundsException("Insufficient Funds")
        self.__balance -= amount


    def get_number(self):
        return self.__account_number
    def is_pin_not_valid(self, pin):
        return pin != self.__account_pin

    def __is_amount_valid(self, amount):
        return amount < 0

    def __is_balance_insufficient(self, amount):
        return amount > self.__balance
