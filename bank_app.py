from bank import Bank
from invalid_pin_exception import InvalidPinException
from tkinter import simpledialog, messagebox


class BankApp:
    def __init__(self):
        self.bank = Bank("Ajibola'd Bank")

    def display(self):
        print("")
        user_response = BankApp.user_input("""
        <><><><><><><> WELCOME TO AJIBOLA'S Bank <><><><><><><><><>
            The best bank you can ever think of :)
            [<1>] sign in with account number   [<2>] create an account
            
                            [<3>] Exit Bank
        """)
        match user_response:
            case "1":
                try:

                    account = self.bank.find_account(int(BankApp.user_input("Enter Your Account Number")))
                    self.display_what_user_can_do(account)
                except Exception as e:
                    BankApp.output(e)
                    BankApp.output("Create An Account With us Today ")
                    self.display()
            case "2":
                try:
                    self.create_account()
                    account = self.bank.find_account(int(BankApp.user_input("Enter Your Account Number")))
                    self.display_what_user_can_do(account)
                except Exception as e:
                    BankApp.output(f"{e}")
                    self.display()
            case "3":
                BankApp.output("Thank you for choosing our bank \nthe best bank app ever \nGood-Bye")
            case _:
                BankApp.output("Wrong Input")
                self.display()

    def create_account(self):
        first_name = BankApp.user_input("Enter first name: ")
        last_name = BankApp.user_input("Enter last name: ")
        pin = BankApp.user_input("Enter pin: ")
        try:
            self.verify_pin(pin)
        except Exception as e:
            BankApp.output(e)
            self.create_account()
        account = self.bank.register_customer(first_name, last_name, pin)
        BankApp.output("Customer register successfully!")
        BankApp.output(f"Your account number is {account.get_number()}")

    def deposit(self):
        account = None
        try:
            account = self.bank.find_account(int(BankApp.user_input("Enter your account number: ")))
            amount = int(BankApp.user_input("Enter an amount: "))
            account.deposit(amount)
            BankApp.output("Amount deposited successfully!")
        except Exception as e:
            BankApp.output(e)
        finally:
            self.display_what_user_can_do(account)

    def transfer(self):
        account = None
        try:
            account = self.bank.find_account(int(BankApp.user_input("Enter your account: ")))
            receiver_account = self.bank.find_account(int(BankApp.user_input("Enter the receiver account number: ")))
            amount = int(BankApp.user_input("Enter transfer amount: "))
            pin = BankApp.user_input("Enter your pin: ")
            account.withdraw(amount, pin)
            receiver_account.deposit(amount)
            BankApp.output("Amount transferred successfully!")
        except Exception as e:
            BankApp.output(e)
        finally:
            self.display_what_user_can_do(account)

    def withdraw(self):
        account = None
        try:
            account = self.bank.find_account(int(BankApp.user_input("Enter your account number: ")))
            amount = int(BankApp.user_input("Enter the amount: "))
            pin = BankApp.user_input("Enter your pin: ")
            account.withdraw(amount, pin)
            BankApp.output("Amount withdrawn successfully!")
        except Exception as e:
            BankApp.output(e)
        finally:
            self.display_what_user_can_do(account)

    def check_balance(self):
        account = None
        try:
            account = self.bank.find_account(int(BankApp.user_input("Enter your account number: ")))
            pin = BankApp.user_input("Enter your pin: ")
            BankApp.output(f"Your balance is:{account.check_balance(pin)}")
        except InvalidPinException as e:
            BankApp.output(e)
        finally:
            self.display_what_user_can_do(account)

    def close_account(self):
        account = None
        try:
            account = self.bank.find_account(int(BankApp.user_input("Enter the account number: ")))
            pin = BankApp.user_input("Enter your pin: ")
            self.bank.remove_account(account, pin)
            BankApp.output("Account closed successfully!")
        except InvalidPinException as e:
            BankApp.output(e)
            self.display_what_user_can_do(account)

    @staticmethod
    def exit():
        BankApp.output("Exit")
        return

    @staticmethod
    def output(prompt):
        messagebox.showinfo("Output", prompt)

    @staticmethod
    def user_input(prompt):
        return simpledialog.askstring("Input", prompt)

    def display_what_user_can_do(self, account):
        user_response = BankApp.user_input(f""" 
        <<<<<<< Welcome Your account number is {account.get_number()}>>>>>>>>>>>>
                    What Do You Want To Do With Us Today :)
                    
          [<1>] Deposit                 [<2>]    Withdraw
          
          [<3>] Check Balance           [<4>]    Transfer
          
          [<5>] Close Bank              [<6>]    Back
        """)
        match user_response:
            case "1":
                self.deposit()
            case "2":
                self.withdraw()
            case "3":
                self.check_balance()
            case "4":
                print("yes")
                self.transfer()
            case "5":
                self.close_account()
                self.display()
            case "6":
                self.display()
            case _:
                BankApp.output("Wrong Input")
                self.display()

    @staticmethod
    def verify_pin(pin):
        verified_pin = BankApp.user_input("Verify Pin")
        if pin != verified_pin: raise InvalidPinException("Pin MisMatch")


def main():
    bank_app = BankApp()
    bank_app.display()


if __name__ == "__main__":
    main()
