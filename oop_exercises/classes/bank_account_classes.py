class BankAccount:

    def __init__(self, account_id, username, password, account_holder, balance):
        self.account_id = account_id
        self.username = username
        self.password = password
        self.account_holder = account_holder
        self.balance = balance

    def account_details(self):
        print("\nAccount ID: " + self.account_id)
        print("Account Name: " + self.account_holder)

    def check_balance(self):
        print("\nYour current balance is " + str(self.balance))

    def deposit_money(self):
        while True:
            user_deposit = int(input("\nHow much would you like to deposit? "))
            if user_deposit <= 100:
                print("\nThe minimum amount to deposit is 500PHP")
            else:
                self.balance += user_deposit
                print("\nYour new balance is " + str(self.balance))
                break

    def withdraw_money(self):
        user_draw = int(input("How much would you like to withdraw? "))
        if user_draw > self.balance:
            print("You do not have enough balance to withdraw that amount.")
        elif user_draw == self.balance:
            choice = input("Are you sure you want to withdraw all your remaining balance (Yes/No)?").lower()
            if choice == "yes":
                self.balance -= user_draw
                print("Your new balance is " + str(self.balance))
            else:
                pass
        else:
            self.balance -= user_draw
            print("Your new balance is " + str(self.balance))
