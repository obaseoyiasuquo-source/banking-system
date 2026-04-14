accounts = {}

def create_account():
    acct_no = input("Please input your account number: ")
    acct_name = input("Please input your name: ")
    init_amount = 0

    if acct_no not in accounts:
        accounts[acct_no] = {"Account Name": acct_name, "Balance": init_amount}
        print(f"{acct_no} belonging to {acct_name} created successfully!")
    else:
        print("Account already exists!")

def view_balance():
    acct_no = input("Please input your account number: ")
    if acct_no not in accounts:
        print("Account does not exist.")
    else:
        for acct_no, details in accounts.items():
            name = details["Account Name"]
            balance = details["Balance"]
            print(f"\nAccount Number: {acct_no}")
            print(f"\nAccount Name: {name}")
            print(f"\nBalance: ${balance}")

def deposit():
    acct_no = input("Please enter your account number: ")
    if acct_no not in accounts:
        print("Account doesn't exist.")
    else:
        amount = int(input("How much would you like to deposit? $"))
        if amount <= 0:
            print("Invalid amount. Amount must be greater than zero.")
        else:
            accounts[acct_no]["Balance"] += amount
            print(f"Deposit of ${amount} successful!")
            name = accounts[acct_no]["Account Name"]
            balance = accounts[acct_no]["Balance"]
            print(f"\nAccount Number: {acct_no}")
            print(f"\nAccount Name: {name}")
            print(f"\nNew Balance: ${balance}")

def withdraw():
    acct_no = input("Please enter your account number: ")
    if acct_no not in accounts:
        print("Account doesn't exist.")
    else:
        amount = int(input("How much would you like to withdraw? $"))
        if amount <= 0:
            print("Invalid amount. Amount must be greater than zero.")
        else:
            accounts[acct_no]["Balance"] -= amount
            print(f"Withdrawal of ${amount} successful!")
            name = accounts[acct_no]["Account Name"]
            balance = accounts[acct_no]["Balance"]
            print(f"\nAccount Number: {acct_no}")
            print(f"\nAccount Name: {name}")
            print(f"\nNew Balance: ${balance}")

def exit_app():
    while True:
        options = input("Would you like to exist? Y/N ").lower()
        if options == "y":
            print("Exiting app... ")
            exit()
        elif options == "n":
            break
        else:
            print("Invalid Command")


def main():
    print("\n --- Welcome to MyBank --- ")
    print("\n1. Create account")
    print("\n2. View Balance")
    print("\n3. Deposit")
    print("\n4. Withdraw")
    print("\n5. Exit app")

    while True:
        selection = input("What would you like to do? ")
        
        if selection == "1":
            create_account()
        elif selection == "2":
            view_balance()
        elif selection == "3":
            deposit()
        elif selection == "4":
            withdraw()
        elif selection == "5":
            exit_app()
        else:
            print("Invalid command. Please select an option from 1-5. ")

if __name__ == "__main__":
    main()