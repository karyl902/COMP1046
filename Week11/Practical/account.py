#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
import icontract


class Account:
    minimum_balance = 1000

    @icontract.require(lambda initial_balance: initial_balance >= Account.minimum_balance)
    def __init__(self, initial_balance):
        self.balance = initial_balance

    @icontract.ensure(lambda self, sum: self.balance == self.balance - sum + sum)
    def __add__(self, sum):
        self.balance = self.balance + sum

    @icontract.require(lambda sum: sum >= 0)
    @icontract.ensure(lambda self, sum: self.balance == self.balance - sum + sum)
    def deposit(self, sum):
        self.__add__(sum)

    @icontract.require(lambda sum: sum >= 0)
    @icontract.require(lambda self, sum: sum <= self.balance - self.minimum_balance)
    @icontract.ensure(lambda self, sum: self.balance == self.balance + sum - sum)
    def withdraw(self, sum):
        self.__add__(-sum)

    def may_withdraw(self, sum):
        return (self.balance - sum) >= Account.minimum_balance


# TEST:
a = Account(1000)
a.deposit(1200)
print("Current balance: " + str(a.balance))
a.withdraw(200)
print("Current balance: " + str(a.balance))
print("May withdraw 200? " + str(a.may_withdraw(200)))

a = Account(1999)
a = Account(1000)
a.deposit(100) 
a.withdraw(1)  
a = Account(1000) 
a.deposit(1) 
