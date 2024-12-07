class Account:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print(f"Amount must be a positive number")
        else:
            self.balance += amount
            print(f"Amount added - {amount}. New balance - {self.balance}")
    
    def withdraw(self, amount):
        if amount < 0:
            print(f"Amount withdrawn can be less than zero.")
        else:
            self.balance -= amount
            print(f"Amount withdrawn - {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance
    
class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate = 0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
         interest = self.balance * self.interest_rate
         print(f"Interest for acc number {self.account_number} is - {interest}")
         return interest
    
    def apply_interest(self):
        interest = self.calculate_interest()
        self.balance += interest

        print(f"Applied interest {interest}. New balance {self.balance}")
    

class CheckingAccount(Account):
    def __init__(self, account_number, balance = 0, overdraft_limit = 500):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdraw: {amount}. New balance : {self.balance}")
        else:
            print(f"Overdraft limit crossed.")

def main():
    #create saving account
    savings = SavingsAccount("S123", 500, 0.03)
    savings.deposit(500)
    savings.calculate_interest()
    savings.apply_interest()
    savings.withdraw(200)

    print(f"Savings account balance - {savings.get_balance()}")

    #create checking acc
    checking = CheckingAccount("C123", 500, 500)
    checking.deposit(500)
    checking.withdraw(200)
    checking.withdraw(5000)
    print(f"Checking acc balance: {checking.get_balance()}")

if __name__ == "__main__":
    main()

