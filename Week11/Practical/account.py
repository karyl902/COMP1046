class Account:
    minimum_balance = 1000

    def __init__(self,initial_balance):
        self.balance = initial_balance

    def __add__(self, sum):
        self.balance = self.balance + sum
    
    def deposit(self,sum):
        self.__add__(sum)

    def withdraw(self,sum):
        self.__add__(-sum)

    def may_withdraw(self,sum):
        return (self.balance-sum)>=Account.minimum_balance

#TEST:
a = Account(1000)
a.deposit(1200)
print("Current balance: " + str(a.balance))
a.withdraw(200)
print("Current balance: " + str(a.balance))
print("May withdraw 200? " + str(a.may_withdraw(200)))