class Account:
    #define __init__ to instantiate member variable.
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Debit amount exceeds account balance. Balance remains unchanged."

    def get_balance(self):
        return f"Current balance: ${self.balance}"

# Example usage:
if __name__ == "__main__":
    account = Account(1000)  # Initial balance of $1000
    print(account.get_balance())
    print(account.deposit(500))
    print(account.debit(200))
    print(account.debit(1500))
    print(account.get_balance())
