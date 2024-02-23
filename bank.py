from account import Account
from account_does_not_exist_exception import AccountNotFoundException
from invalid_pin_exception import InvalidPinException


class Bank:
    def __init__(self, bank_name):
        self.__name = bank_name
        self.__accounts = []
        self.__account_number = 0

    def register_customer(self, first_name: str, last_name: str, pin: str) -> Account:
        account = Account(first_name + " " + last_name, self.__generate_account_number(), pin)
        self.__add_account_to_bank(account)
        return account

    def number_of_customers(self) -> int:
        return self.__account_number

    def __generate_account_number(self) -> int:
        self.__account_number = self.__account_number + 1
        return self.__account_number

    def __add_account_to_bank(self, account: Account) -> None:
        self.__accounts.append(account)

    def find_account(self, account_number: int) -> Account:
        for account in self.__accounts:
            if account_number == account.get_number():
                return account
        raise AccountNotFoundException("Account Does Not Exist")

    def remove_account(self, account1: Account, pin: str) -> None:
        if account1 not in self.__accounts: raise AccountNotFoundException("Account Does Not Exist ")
        if account1.is_pin_not_valid(pin): raise InvalidPinException("Invalid Pin ")
        self.__accounts.remove(self.find_account(account1.get_number()))

    def get_number_of_active_account(self) -> int:
        return len(self.__accounts)

    def deposit(self, account_number: int, amount: int):
        account = self.find_account(account_number)
        account.deposit(amount)

    def check_balance(self, account_number: int, pin: str) -> int:
        account = self.find_account(account_number)
        if account.is_pin_not_valid(pin): raise InvalidPinException("Invalid Pin ")
        return account.check_balance(pin)

    def withdraw(self, account_number: int, amount: int, pin: str):
        account = self.find_account(account_number)
        if account.is_pin_not_valid(pin): raise InvalidPinException("Invalid Pin ")
        return account.withdraw(amount,pin)

    def transfer(self, sender_account_number: int, receiver_account_number: int, amount: int, pin: str) -> None:
        account = self.find_account(sender_account_number)
        account1 = self.find_account(receiver_account_number)
        if account.is_pin_not_valid(pin): raise InvalidPinException("Invalid Pin ")
        account.withdraw(amount, pin)
        account1.deposit(amount)


