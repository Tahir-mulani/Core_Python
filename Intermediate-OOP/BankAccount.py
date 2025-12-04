class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn.")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance


# Creating accounts
acc1 = BankAccount("Tahir", 500)
acc2 = BankAccount("Rahul", 800)

# Transactions
acc1.deposit(1000)
acc2.withdraw(500)

# Final balances
print("Account 1 final balance:", acc1.get_balance())
print("Account 2 final balance:", acc2.get_balance())
