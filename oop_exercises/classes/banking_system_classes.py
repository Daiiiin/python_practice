class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount >= 100:
            self.balance += amount
        else:
            print("The minimum deposit is 100 Php")

    def withdraw(self, amount):
        if amount > self.balance:
            print("You do not have enough balance to withdraw that amount.")
        else:
            self.balance -= amount

    def get_balance(self):
        print("Your balance is " + str(self.balance) + " Php")

    def display_account_info(self):
        print("Account Number: " + self.account_number)
        print("Account Holder: " + self.account_holder)
        print("Balance: " + str(self.balance) + " Php")
