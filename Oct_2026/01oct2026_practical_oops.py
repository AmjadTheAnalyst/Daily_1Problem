# ============================================================
# OOP PRACTICE — BANK ACCOUNT
# ============================================================
#
# Create a BankAccount class that represents a customer's
# bank account.
#
# Your goal is to practice:
# - Classes
# - Objects
# - __init__()
# - self
# - Attributes
# - Methods
# - Changing object state
# - Returning values
# - Basic validation
#
#
# ------------------------------------------------------------
# REQUIREMENT 1 — CREATE THE CLASS
# ------------------------------------------------------------
#
# Create a class called BankAccount.
#
# The class should have these attributes:
#
#   account_holder
#   account_number
#   balance
#
# These values should be received through __init__().
class BankAccount():
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print('This is an invalid amount')
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance = self.balance - amount
            else:
                print('Account does not have sufficient balance')
        else:
            print('Amount can not be 0')
    def check_balance(self):
        print(f'Dear {self.account_holder} you current balance is:\n{self.balance}')
    def display_account(self):
        print(f'Account Holder Name: {self.account_holder}\nAccount Number: {self.account_number}\nTotal Balance: {self.balance}')
account = BankAccount("Ali", "12345", 1000)
#print(account.balance)
#deposit_function = account.deposit(-12)
#account.withdraw(1500)
#account.check_balance()
account.display_account()
#print(account.balance)

'''✅ Bank Account OOP — Successfully created a BankAccount class with attributes, initialization, deposit, withdrawal, balance checking, and account display methods.

🧠 Demonstrated understanding of classes, objects, self, attributes, methods, and changing object state through methods.

🔧 Key improvements: Allow withdrawal of the entire balance by using <= instead of <, print the invalid withdrawal message, and return the balance from check_balance() when the value needs to be used by the caller.

🏆 Score: 9.0/10 | OOP Practice — IN PROGRESS'''
        
# ------------------------------------------------------------
# REQUIREMENT 2 — DEPOSIT
# ------------------------------------------------------------
#
# Create a method:
#
#   deposit(amount)
#
# Rules:
#
# - The amount must be greater than 0.
# - If the amount is valid, add it to the balance.
# - If the amount is 0 or negative, reject the deposit.
#
#
# ------------------------------------------------------------
# REQUIREMENT 3 — WITHDRAW
# ------------------------------------------------------------
#
# Create a method:
#
#   withdraw(amount)
#
# Rules:
#
# - The amount must be greater than 0.
# - The customer cannot withdraw more money than the
#   current balance.
# - If the withdrawal is valid, subtract it from the balance.
# - Otherwise, reject the withdrawal.
#
#
# ------------------------------------------------------------
# REQUIREMENT 4 — CHECK BALANCE
# ------------------------------------------------------------
#
# Create a method:
#
#   check_balance()
#
# It should return the current balance.
#
#
# ------------------------------------------------------------
# REQUIREMENT 5 — DISPLAY ACCOUNT
# ------------------------------------------------------------
#
# Create a method:
#
#   display_account()
#
# It should display:
#
# Account Holder: <name>
# Account Number: <number>
# Balance: <balance>
#
#
# ------------------------------------------------------------
# TEST YOUR CLASS
# ------------------------------------------------------------
#
# Create the following object:
#
# account = BankAccount("Ali", "12345", 1000)
#
# Then perform these operations:
#
# 1. Deposit 500
# 2. Withdraw 200
# 3. Check the balance
# 4. Display the account information
#
#
# ------------------------------------------------------------
# EXPECTED FINAL BALANCE
# ------------------------------------------------------------
#
# 1300
#
#
# ------------------------------------------------------------
# EXTRA TESTS
# ------------------------------------------------------------
#
# After your main test works, also test:
#
# - Deposit 0
# - Deposit -100
# - Withdraw 0
# - Withdraw -50
# - Withdraw more than the current balance
#
# Make sure your program handles these cases correctly.
#
# ============================================================
# WRITE YOUR SOLUTION BELOW
# ============================================================

class BankAccount:
    pass


# Create your object and test your methods here.