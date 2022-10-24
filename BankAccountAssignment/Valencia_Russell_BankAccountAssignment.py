class BankAccount:
    all_banks = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
        # your code here
    def withdraw(self, amount):
        self.balance = self.balance - amount
        # your code here
        return self
    def display_account_info(self):
        print(self.balance)
        print(self.int_rate)
        # your code here
    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        return self
        # your code here

    @classmethod
    def all_banks_info(cls):
        sum = 0
        for bank in cls.all_banks:
            sum += bank.balance

BankAccount.all_banks_info()

IzukuMidoriya = BankAccount(0.05, 3600)
KatsukiBakugo = BankAccount(0.8, 2350)

IzukuMidoriya.deposit(60).deposit(350).deposit(800).yield_interest().display_account_info()

KatsukiBakugo.deposit(500).deposit(650).withdraw(200).withdraw(50).withdraw(10).withdraw(25).yield_interest().display_account_info()
