class Bank_account:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        Bank_account.accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        print(f"Successful deposit of ${amount}")
        return self

    def withdraw(self,amount):
        if self.balance < amount:
            print(f"Insufficient funds, cannot withdraw ${amount}")
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Account balance: {self.balance} -- Account interest rate: {self.int_rate}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
            return self

    @classmethod
    def print_all_accounts(cls):
        for i in cls.accounts:
            i.display_account_info()


checking = Bank_account(.03,500)
savings = Bank_account(.05,10000)

checking.deposit(100).deposit(10).deposit(50).withdraw(400).yield_interest().display_account_info()
savings.deposit(500).deposit(300).withdraw(100).withdraw(400).withdraw(200).withdraw(50).yield_interest().display_account_info()

Bank_account.print_all_accounts()