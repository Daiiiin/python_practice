from classes.bank_account_classes import BankAccount

def main(account):
    print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money")
    choose = int(input("What would you like to do (1,2,3)? "))
    if choose == 1:
        account.check_balance()
    elif choose == 2:
        account.deposit_money()
    elif choose == 3:
        account.withdraw_money()
    else:
        pass


account_1 = BankAccount("10001", "Matthew Desabelle", 1000)
account_2 = BankAccount("10002", "Sam Abrigos", 1000)
account_3 = BankAccount("10003", "Joshua Soqueno", 1000)
account_4 = BankAccount("10004", "Neil Torre", 1000)
account_5 = BankAccount("10005", "Tricia Alcisto", 1000)

# User open their account
user_account = str(input("Enter your account ID: "))
if user_account == account_1.account_id:
    account_1.account_details()
    main(account_1)
elif user_account == account_2.account_id:
    account_2.account_details()
    main(account_2)
elif user_account == account_3.account_id:
    account_3.account_details()
    main(account_3)
elif user_account == account_4.account_id:
    account_4.account_details()
    main(account_4)
elif user_account == account_5.account_id:
    account_5.account_details()
    main(account_5)
else:
    print("The account does not exist.")
