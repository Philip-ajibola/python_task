from bank import Bank
from invalid_pin_exception import InvalidPinException
from account_does_not_exist_exception import AccountNotFoundException
from insufficient_funds_exception import InsufficientFundsException
from invalid_amount_exception import InvalidAmountException


class BankApp:
    def __init__(self):
        self.bank = Bank("Ajibola'd Bank")

    def display(self):
        print("")
        print("Bank App")
        print("1.Create customer\n2.Close Account\n3.Deposit \n4.Transfer \n5.Withdraw\n6.Check balance "
              "\n7.Exit App")
        print("*")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.create_account()
        elif choice == "2":
            self.close_account()
        elif choice == "3":
            self.deposit()
        elif choice == "4":
            self.transfer()
        elif choice == "5":
            self.withdraw()
        elif choice == "6":
            self.check_balance()
        elif choice == "7":
            self.exit()
        else:
            print("Enter valid choice")
            self.display()

    def create_account(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Enter pin: ")
        account = self.bank.register_customer(first_name, last_name, pin)
        print("Customer register successfully!")
        print("Account Number: ", account.get_number())
        self.display()

    def deposit(self):
        try:
            account = None
            try:
                account_number = int(input("Enter your account number: "))
                account = self.bank.find_account(account_number)
            except Exception as e:
                print(e)
                self.display()
            amount = int(input("Enter an amount: "))
            account.deposit(amount)
            print("Amount deposited successfully!")
        except Exception as e:
            print(e)
        finally:
            self.display()

    def transfer(self):
        try:
            amount = int(input("Enter transfer amount: "))
            sender_account = self.bank.find_account( int(input("Enter your account: ")))
            receiver_account = self.bank.find_account(int(input("Enter the receiver account number: ")))
            pin = input("Enter your pin: ")
            sender_account.withdraw(amount,pin)
            print("Amount transferred successfully!")
        except Exception as e:
            print(e)
        finally:
            self.display()

    def withdraw(self):
        try:
            account = self.bank.find_account(int(input("Enter your account number: ")))
            amount = int(input("Enter the amount: "))
            pin = input("Enter your pin: ")
            account.withdraw(amount,pin)

            print("Amount withdrawn successfully!")
        except Exception as e:
            print(e)
        finally:
            self.display()

    def check_balance(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        try:
            balance = self.bank.check_balance(int(account_number), pin)
            print("Your balance is:", balance)
        except InvalidPinException as e:
            print(e)
        finally:
            self.display()

    def close_account(self):
        account_number = int(input("Enter the account number: "))
        pin = input("Enter your pin: ")
        try:
            self.bank.remove_account(account_number, pin)
            print("Account closed successfully!")
        except InvalidPinException as e:
            print(e)

    @staticmethod
    def exit():
        print("Exit")
        return


def main():
    bank_app = BankApp()
    bank_app.display()


if __name__ == "__main__":
    main()
