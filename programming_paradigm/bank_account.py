'''
Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. Use command line arguments to interact with instances of this class.

Task Description:
You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, which interfaces with the class through command line arguments to perform banking operations.

bank_account.py:
Class Definition:

Define a class named BankAccount.
Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
Encapsulation and Behaviors:

Implement deposit(amount), withdraw(amount), and display_balance() methods.
deposit should add the specified amount to account_balance.
withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
display_balance should print the current balance in a user-friendly format.

'''

class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        pass

    def deposit(self, amount):
    
        return self.account_balance + amount
    

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance-= amount 
            return True
        else: 
            return False
        

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")    