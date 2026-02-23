from random import randint

accounts = []
MIN_BALANCE = 500


def create_account():
    while True:
        account_number = randint(1000, 9999)
        duplicate_found = False

        for account in accounts:
            if account['acc_num'] == account_number:
                duplicate_found = True
                break

        if not duplicate_found:
            break
    while True:
        name = input("Enter account holder's name: ").strip()

        if not name:
            print("Name cannot be empty!")
            continue
        if not name.replace(" ", "").isalpha():
            print("Name should contain only alphabets and spaces!")
            continue

        break
        

    while True:
        try:
            amount = float(input(f"Deposit minimum {MIN_BALANCE} INR: "))
            
            if amount < MIN_BALANCE:
                print(f"Minimum deposit is {MIN_BALANCE} INR")
                continue

            break

        except ValueError:
            print("Please enter numbers only!")

    account = {
        'acc_num': account_number,
        'name': name,
        'balance': amount
    }

    accounts.append(account)

    print(f"\nAccount successfully created!")
    print(f"Account Number: {account_number}")
    print(f"Account Holder: {name}")
    print(f"Current Balance: ₹{amount:.2f}")


def find_account(account_number):
    for account in accounts:
        if account_number == account['acc_num']:
            return account
    return None


def deposit():
    account_number = int(input("Enter your account number: "))
    account = find_account(account_number)

    if account is None:
        print("Account not found!")
        return

    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print(f"{amount} can't be deposited!")
        return

    account['balance'] += amount
    print("Deposit Successful!")
    print(f"Your updated balance is ₹{account['balance']:.2f}")


def withdraw():
    account_number = int(input("Enter your account number: "))
    account = find_account(account_number)

    if account is None:
        print("Account not found!")
        return

    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Amount must be greater than 0!")
        return

    if account['balance'] - amount < MIN_BALANCE:
        print(f"Minimum balance of {MIN_BALANCE} INR must be maintained!")
        return

    account['balance'] -= amount
    print("Withdrawal Successful!")
    print(f"Remaining balance: ₹{account['balance']:.2f}")


def check_balance():
    account_number = int(input("Enter your account number: "))
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