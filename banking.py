class BankAccount:
    def __init__(self, acct_no, acct_name, balance=0):
        self.acct_no = acct_no
        self.acct_name = acct_name
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Amount must be greater than zero.")
        else:
            self._balance += amount
            print(f"${amount} deposited successfully!")
        

    def withdraw(self, amount):   
        if amount <= 0:
            print("Invalid amount. Amount must be greater than zero!")
        elif amount > self._balance:
            print("Insufficient funds for this transaction.")
        else:
            self._balance -= amount
            print(f"${amount} withdrawn successfully!")
        
        

    def display(self):   
            print(f"\nAccount Number: {self.acct_no}")
            print(f"Acoount Name: {self.acct_name}")
            print(f"Acoount Balance: ${self._balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acct_no = input("Please input your account number: ")
        acct_name = input("Please enter your name: ")

        if acct_no in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[acct_no] = BankAccount(acct_no, acct_name)
            print(f"Account belonging to {acct_name} created successfully! ")
    
    def get_account(self, acct_no):
        return self.accounts.get(acct_no)
    
    def deposit(self):
        acct_no = input("Please enter your account number: ")
        account = self.get_account(acct_no)

        if not account:
            print("Account doesn't exist!")
            return
        
        amount = int(input("Please enter deposit amount: $"))
        account.deposit(amount)
        account.display()

    def withdraw(self):
        acct_no = input("Please enter your account number: ")
        account = self.get_account(acct_no)

        if not account:
            print("Account does not exist!")
            return    

        amount = int(input("Please enter amount to be withdrawn: $"))
        account.withdraw(amount)
        account.display()

    def view_balance(self):
        acct_no = input("Please enter your account number: ")
        account = self.get_account(acct_no)

        if not account:
            print("Account does not exist!")
        else:
            account.display()
        

def main():
    print("\n --- Welcome to MyBank --- ")
    print("\n1. Create account")
    print("\n2. View Balance")
    print("\n3. Deposit")
    print("\n4. Withdraw")
    print("\n5. Exit app")

    bank = Bank()
    while True:
        
        selection = input("What would you like to do? ")
        
        if selection == "1":
            bank.create_account()
        elif selection == "2":
            bank.view_balance()
        elif selection == "3":
            bank.deposit()
        elif selection == "4":
            bank.withdraw()
        elif selection == "5":
            break
        else:
            print("Invalid command. Please select an option from 1-5. ")

if __name__ == "__main__":
    main()