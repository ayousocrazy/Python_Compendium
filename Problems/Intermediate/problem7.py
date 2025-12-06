"""
Mini Banking System
Design a class BankAccount with methods:
    deposit(amount)
    withdraw(amount)
    get_balance()

Add:
-Data validation using conditionals.
-A loop-based mini menu system to test it:
1. Deposit
2. Withdraw
3. Show Balance
4. Exit
"""

class BankAccount:
    def __init__(self, name, nin, balance):
        self.name = name
        self.__nin = nin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Deposit failed. Amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal failed. Amount must be positive.")
            return

        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance

name = input("Enter your name: ")
nin = input("Enter your National Identity Card Number: ")

balance = float(input("Enter balance to open an account (minimum 100): "))

while balance < 100:
    balance = float(input("Minimum is 100. Enter again: "))

user = BankAccount(name, nin, balance)

while True:
    print("\n--- Banking Menu ---")
    print("(1) Deposit")
    print("(2) Withdraw")
    print("(3) Show Balance")
    print("(4) Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            try:
                amt = float(input("Amount to deposit: "))
                user.deposit(amt)
            except:
                print("Invalid input.")

        case "2":
            try:
                amt = float(input("Amount to withdraw: "))
                user.withdraw(amt)
            except:
                print("Invalid input.")

        case "3":
            print(f"Your current balance is: {user.get_balance()}")

        case "4":
            print("Exiting. Goodbye!")
            break

        case _:
            print("Invalid choice. Try again.")