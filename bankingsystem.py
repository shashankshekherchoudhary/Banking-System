from random import randint
from datetime import datetime

accounts = []
MIN_BALANCE = 500


# -------------------- Helper Functions --------------------

def get_int_input(message):
    while True:
        try:
            return int(input(message).strip())
        except ValueError:
            print("Please enter numbers only!")


def get_float_input(message):
    while True:
        try:
            return float(input(message).strip())
        except ValueError:
            print("Please enter numbers only!")


def find_account(account_number):
    for account in accounts:
        if account['acc_num'] == account_number:
            return account
    return None


def get_valid_account():
    while True:
        account_number = get_int_input("Enter your 4-digit account number: ")

        if account_number < 1000 or account_number > 9999:
            print("Account number must be a 4-digit number!")
            continue

        account = find_account(account_number)

        if account is None:
            print("Account not found! Please try again.")
            continue

        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ").strip()

            if not entered_pin.isdigit():
                print("PIN must contain numbers only!")
                continue

            if entered_pin == account['pin']:
                return account

            attempts -= 1

            if attempts == 0:
                print("Too many incorrect attempts. Returning to menu.\n")
            else:
                print(f"Incorrect PIN! Attempts left: {attempts}")

        return None


# -------------------- Core Functions --------------------

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
        amount = get_float_input(f"Deposit minimum {MIN_BALANCE} INR: ")

        if amount < MIN_BALANCE:
            print(f"Minimum deposit is {MIN_BALANCE} INR")
            continue

        break

    while True:
        pin = input("Set 4-digit PIN: ").strip()

        if not pin:
            print("PIN cannot be blank!")
            continue

        if not pin.isdigit():
            print("PIN must contain numbers only!")
            continue

        if len(pin) != 4:
            print("PIN must be exactly 4 digits!")
            continue

        break

    account = {
        'acc_num': account_number,
        'name': name,
        'balance': amount,
        'pin': pin,
        'transaction_history': []
    }

    accounts.append(account)

    print("\nAccount successfully created!")
    print(f"Account Number: {account_number}")
    print(f"Account Holder: {name}")
    print(f"Current Balance: ₹{amount:.2f}")


def deposit():
    account = get_valid_account()
    if account is None:
        return

    amount = get_float_input("Enter amount to deposit: ")

    if amount <= 0:
        print("Amount must be greater than 0!")
        return

    account['balance'] += amount

    account['transaction_history'].append({
        'type': 'deposit',
        'amount': amount,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'balance_after': account['balance']
    })

    print("Deposit Successful!")
    print(f"Your updated balance is ₹{account['balance']:.2f}")


def withdraw():
    account = get_valid_account()
    if account is None:
        return

    amount = get_float_input("Enter amount to withdraw: ")

    if amount <= 0:
        print("Amount must be greater than 0!")
        return

    if account['balance'] - amount < MIN_BALANCE:
        print(f"Minimum balance of {MIN_BALANCE} INR must be maintained!")
        return

    account['balance'] -= amount

    account['transaction_history'].append({
        'type': 'withdraw',
        'amount': amount,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'balance_after': account['balance']
    })

    print("Withdrawal Successful!")
    print(f"Remaining balance: ₹{account['balance']:.2f}")


def check_balance():
    account = get_valid_account()
    if account is None:
        return

    print(f"Your current balance is: ₹{account['balance']:.2f}")


def view_transactions():
    account = get_valid_account()
    if account is None:
        return

    if not account['transaction_history']:
        print("No transactions found.")
        return

    print("\n--- Transaction History ---")
    for txn in account['transaction_history']:
        print(f"{txn['timestamp']} | {txn['type'].title()} | ₹{txn['amount']} | Balance: ₹{txn['balance_after']:.2f}")


# -------------------- Menu --------------------

def menu():
    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Exit")

        choice = get_int_input("Enter your choice: ")

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            view_transactions()
        elif choice == 6:
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice! Please try again.")


menu()