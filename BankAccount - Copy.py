from abc import ABC, abstractmethod

class BankAccount(ABC):
    # Constant variable for the bank name
    BANK_NAME = "MyBank"

    @abstractmethod
    def deposit(self, amount: int):
        pass

    @abstractmethod
    def withdrawal(self, amount: int):
        pass

    @abstractmethod
    def get_balance(self) -> int:
        pass

class Account(BankAccount):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount: int):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdrawal(self, amount: int):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self) -> int:
        return self.balance

# Example usage:
account = Account()
print(f"Bank Name: {account.BANK_NAME}")
account.deposit(1000)
account.withdrawal(500)
print(f"Current Balance: ${account.get_balance()}")
