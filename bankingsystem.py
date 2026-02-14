from random import randint
accounts = []
def create_account ():
    account_number = randint(1000,9999)
    name = input("Enter account holder's name : ")
    balance = float(input("Deposit minimnun 500 INR : "))

    account = {
        'acc_num' : account_number ,
        'name' : name ,
        'balance' : balance
    }

    accounts.append(account)
    print(f"{account_number} is successfully created!")

