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
    for account in accounts:
        if account_number == account['acc_num']:
            return account
    return None


def deposit():
    account_number = int(input("Enter your account number : "))
    account = find_account(account_number)
    
    if account is None:
        print("Account not found!")
        return
    

    amount = float(input("Enter amount to deposit : "))
    account['balance'] += amount
    print("Deposit Successfull!")
    print(f"Your updated balance is {account['balance']}")

def withdraw():
    account_number = int(input("Enter your account number : "))
    account = find_account(account_number)

    if account is None:
        print("Account not found!")
        return

    amount = float(input("Enter amount to withdraw : "))

    if amount <= 0:
        print("Amount must be greater than 0!")
        return

    if amount > account['balance']:
        print("Insufficient balance!")
        return

    account['balance'] -= amount
    print("Withdrawal Successful!")
    print(f"Remaining balance: {account['balance']}")

def check_balance():
    account_number = int(input("Enter your account number : "))
    account = find_account(account_number)

    if account is None:
        print("Account not found!")
        return
    
    print(f"Your current balance is: ₹{account['balance']:.2f}")


def menu():
    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice! Please try again.")

menu()