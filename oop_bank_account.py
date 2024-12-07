class Account:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance +=  amount
            print(f"Deposited {amount}. New balance - {self.balance}")
        else:
            print(f"Deposit amount must be positive")
        
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            print(f"withdraw amount - {amount}, new balance {self.balance}")
        else:
            print(f"Withdraw amount must be positive")
    
    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance = 0, interest_rate = 0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest for account {self.account_number} : {interest}")
        return interest
    
    def apply_interest(self):
        interest = self.calculate_interest()
        self.balance += interest
        print(f"Applied interest {interest} , new balance {self.balance}")

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit = 500):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance: {self.balance}")
        else:
            print(f"Invalid withdraw amount or exceeds overdraft limit")


# Example usage
def main():
    # Create a savings account
    savings = SavingsAccount(account_number="S123", balance=1000, interest_rate=0.03)
    savings.deposit(500)
    savings.calculate_interest()
    savings.apply_interest()
    savings.withdraw(300)
    print(f"Savings Account Balance: {savings.get_balance()}")

    # Create a checking account
    checking = CheckingAccount(account_number="C123", balance=200, overdraft_limit=1000)
    checking.deposit(300)
    checking.withdraw(400)
    checking.withdraw(1500)  # Exceeds overdraft limit
    print(f"Checking Account Balance: {checking.get_balance()}")

if __name__ == "__main__":
    main()
