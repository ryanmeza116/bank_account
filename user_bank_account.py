class BankAccount:
    intRate = 0.02
    balance = 0
    bankName = "First Bank of Dojo"

    def __init__(self,intRate,balance):
        self.intRate = intRate
        self.balance = balance

    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw (self,amount):
        withdrawalAmount = amount
        self.balance -= withdrawalAmount
        # print("New balance after withdraw :", self.balance)
        return self

# How can i add a $ sign to end of self.balance
    def displayAccountInfo(self):
        return f"Your current account balance is {self.balance}$"
        
    
    def yieldInterest(self):
        # print("Before interest", self.balance)
        x = self.balance * self.intRate
        self.balance += x
        # print("After interest", self.balance)
        return self