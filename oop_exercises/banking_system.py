from classes.banking_system_classes import BankAccount

if __name__ == '__main__':
    account_1 = BankAccount("10001",
                            "Matthew Desabelle",
                            1000)

    account_2 = BankAccount("10002",
                            "John Doe",
                            1500)

    print("Account 1:")
    account_1.display_account_info()
    print("\nDeposit 4500 Php")
    account_1.deposit(4500)
    account_1.get_balance()
    print("\nWithdraw 1450 Php")
    account_1.withdraw(1450)
    account_1.get_balance()

    print("\nAccount 2:")
    account_2.display_account_info()
    print("\nDeposit 50 Php")
    account_2.deposit(50)
    account_2.get_balance()
    print("\nWithdraw 2000 Php")
    account_2.withdraw(2000)
    account_2.get_balance()
    print("\nDeposit 7100 Php")
    account_2.deposit(7100)
    account_2.get_balance()
    print("\nWithdraw 4300 Php")
    account_2.withdraw(4300)
    account_2.get_balance()
