from dataclasses import dataclass
from decimal import Decimal


@dataclass(order=True)
class Account:
    name: str
    balance: Decimal

    def withdraw(self, amount: Decimal):
        if amount <= 0: raise ValueError("Invalid Amount ")
        self.balance -= amount


account = Account("philip", Decimal(100000))
account.withdraw(Decimal(10000))
print(account.balance)

