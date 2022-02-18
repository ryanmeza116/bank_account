class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_withdrawal(self,amount):
        if self.account_balance < amount:
            print(f"Insufficient funds! Cannot withdraw ${amount}")
        else:
            self.account_balance -= amount
            print(f"Successful withdrawal of ${amount}")
        print(f"After withdrawal, current balance is ${self.account_balance}")
        return self

    def make_deposit(self,amount):
        self.account_balance += amount
        print(f"Successful deposit for {self.name} of ${amount}")
        print(f"Current balance after deposit: {self.account_balance}")
        return self

    def display_user_balance(self):
        print(f"Current balance for {self.name} is ${self.account_balance}")
        return self

    def transfer_money(self,other_user,amount):
        if self.account_balance < amount:
            print(f"Insufficient funds, cannot transfer ${amount} to {other_user.name}")
        else:
            self.account_balance -= amount
            other_user.account_balance += amount
            print(f"Successful transfer to {other_user.name} for ${amount} from {self.name}'s account")
            print(f"Current balance for {self.name} : {self.account_balance}")
            print(f"Current balance for {other_user.name} : {other_user.account_balance}")
        return self



ryan = User('Ryan Meza')
abby = User('Abby Meza')



ryan.make_deposit(100).display_user_balance().make_withdrawal(500).transfer_money(abby,25)


print('----------------')
abby.make_deposit(1000).display_user_balance().make_withdrawal(300).transfer_money(ryan,100)


