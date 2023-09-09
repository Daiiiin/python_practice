from classes.bank_account_classes import BankAccount
import pickle
import uuid


# with open("../text_files/bank_account_details.pkl", "wb") as write_file:
#     pickle.dump(account_1, write_file, pickle.HIGHEST_PROTOCOL)

# with open("../text_files/bank_account_details.pkl", "rb") as read_file:
#     account_info = pickle.load(read_file)
#     print(account_info.account_id)
#     print(account_info.account_holder)
#     print(account_info.balance)

# account_list = []
# with open("../text_files/bank_account_details.pkl", "rb") as open_file:
#     try:
#         account_list = pickle.load(open_file)
#     except EOFError:
#         print("Account does not exists. Empty")

# a_id = uuid.uuid4()
# a_name = str(input("Name: "))
# a_username = str(input("Username: "))
# a_password = str(input("Password: "))
#
# account_3 = BankAccount(a_id, a_username, a_password, a_name, 0)
#
# account_list.append(account_3)
#
# print("--------NEW----------")
#
# with open("../text_files/bank_account_details.pkl", "wb") as open_file:
#     pickle.dump(account_list, open_file, pickle.HIGHEST_PROTOCOL)
#
# with open("../text_files/bank_account_details.pkl", "rb") as open_file:
#     account_list = pickle.load(open_file)
#
# for i in range(len(account_list)):
#         print(account_list[i].username)

# print("----Specific----")
#
# for i in range(len(account_list)):
#     if account_list[i].username == "mar":
#         print(account_list[i].username)
#     else:
#         print("not here")

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
            print(opened_account.account_holder)
        else:
            print("Account does not exists.")
    else:
        print("Invalid Input.")


main()


# with open("../text_files/bank_account_details.pkl", "rb") as open_file:
#     account_list = pickle.load(open_file)
#
# for i in range(len(account_list)):
#     print(account_list[i].username)
#
# print("----Specific----")
#
# for i in range(len(account_list)):
#     if account_list[i].username == "bilat":
#         print(account_list[i].username)
#     else:
#         print("not here")