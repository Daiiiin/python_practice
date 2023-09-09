from classes.bank_account_classes import BankAccount
import pickle
import uuid


def create_bank_account():
    account_list = []
    with open("../text_files/bank_account_details.pkl", "rb") as open_file:
        try:
            account_list = pickle.load(open_file)
        except EOFError:
            pass

    account_id = uuid.uuid4()
    account_name = str(input("Enter your name: "))
    account_username = str(input("Enter a username: "))
    account_password = str(input("Enter a password: "))

    new_account = BankAccount(account_id, account_username, account_password, account_name, 0)
    account_list.append(new_account)

    with open("../text_files/bank_account_details.pkl", "wb") as open_file:
        pickle.dump(account_list, open_file, pickle.HIGHEST_PROTOCOL)
        # try:
        #     pickle.dump(account_list, open_file, pickle.HIGHEST_PROTOCOL)
        # except EOFError:
        #     pass


def open_existing_account(username):
    with open("../text_files/bank_account_details.pkl", "rb") as open_file:
        try:
            account_list = pickle.load(open_file)
            for i in range(len(account_list)):
                if account_list[i].username == username:
                    return BankAccount(account_list[i].account_id,
                                       account_list[i].username,
                                       account_list[i].password,
                                       account_list[i].account_holder,
                                       account_list[i].balance)
                else:
                    continue
            else:
                return 0
        except EOFError:
            print("Account does not exists. Empty")


def account_methods(opened_account):
    print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money")
    step_2 = input("\nWhat would you like to do? ")
    if step_2 == "1":
        opened_account.check_balance()
    elif step_2 == "2":
        opened_account.deposit_money()
    elif step_2 == "3":
        opened_account.withdraw_money()
    else:
        print("Invalid Input.")


def main():
    print("1. Create Account\n2. Open Account")
    step_1 = input("\nWhat would you like to do? ")
    if step_1 == "1":
        # create new account()
        create_bank_account()
    elif step_1 == "2":
        # open existing account
        input_username = str(input("Enter your username: "))
        opened_account = open_existing_account(input_username)
        if opened_account != 0:
            opened_account.account_details()
            account_methods(opened_account)
        else:
            print("Account does not exists.")
    else:
        print("Invalid Input.")


main()
