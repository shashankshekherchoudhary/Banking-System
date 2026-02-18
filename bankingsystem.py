from random import randint
accounts = []
def create_account ():
    while True:
        account_number = randint(1000,9999)
        duplicate_found = False
        for account in accounts:
            if account_number == account['acc_num']:
                duplicate_found = True
                break
        if duplicate_found is False:
            break 
    name = input("Enter account holder's name : ")
    balance = float(input("Deposit minimnun 500 INR : "))

    account = {
        'acc_num' : account_number ,
        'name' : name ,
        'balance' : balance
    }

    accounts.append(account)
    print(f"{account_number} is successfully created!")



def find_account(account_number):
    account_found = False
    for account in accounts:
        account_found = True
        if account_number == account['acc_num']:
            return account
        
    if account_found is False:
        return None

