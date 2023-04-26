# Create a BankAccount class with the attributes interest rate and balance
class BankAccount:

    def __init__(self, interest_rate, balance):
        self.balance = balance
        self.interest_rate = interest_rate / 100

# Add a deposit method to the BankAccount class
    def deposit(self, amount):
        self.balance += amount
        return self

# Add a withdraw method to the BankAccount class
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

# Add a display_account_info method to the BankAccount class
    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest Rate: {self.interest_rate * 100}%")
        return self

# Add a yield_interest method to the BankAccount class
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self


# Create 2 accounts
account1 = BankAccount(2, 100)
account2 = BankAccount(3, 200)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
account1.deposit(50).deposit(30).deposit(20).withdraw(40).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
account2.deposit(100).deposit(50).withdraw(20).withdraw(30).withdraw(
    40).withdraw(10).yield_interest().display_account_info()
