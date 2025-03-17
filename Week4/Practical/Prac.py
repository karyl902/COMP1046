#Task1
class Person:
    def __init__(self, name, age, money):
        self.__name = name
        self.__age = age
        self.__alive = True
        self._money = money
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def isAlive(self):
        return self.__alive
    def getMoney(self):
        return self._money
    def setName(self,name):
        self.__name = name
    def haveBirthday(self):
        self.__age += 1
    def spendMoney(self,amount):
        if amount <= self._money:
            self._money -= amount
        else:
            print("Error: Cannot spend that much money")
            return True
    def die(self):
        self.__alive = False
#Task2
import random
class Employee(Person):
    def __init__(self, name, age, money, jobTitle, wage):
        super().__init__(name, age, money)
        self.jobTitle = jobTitle
        self.wage = wage
        self.hours = 0.0
    
    def getJobTitle(self):
        return self.jobTitle
    
    def setWage(self, wage):
        if wage > 0:
            self.wage = wage
    
    def work(self, numHours):
        self.hours += numHours
    
    def receivePay(self):
        if self.isAlive():
            self._money += self.hours * self.wage
            self.hours = 0.0
#task3
class Programmer(Employee):
    def __init__(self, name, age, money, wage):
        super().__init__(name, age, money, 'programmer', wage)
    
    def createCode(self):
        code_examples = [
            "print('hello world')",
            "x=0",
            "raise Exception('What am I doing??')"
        ]
        return random.choice(code_examples)
    
    def work(self, numHours):
        super().work(numHours)
        for _ in range(int(numHours)):
            print(self.createCode())



#Task1 test
girl = Person('Tiffany', 22, 5000.50)
print(girl.getName(), girl.getAge(), girl.getMoney(), girl.isAlive())
girl.haveBirthday()
girl.spendMoney(500)
print(girl.getAge(), girl.getMoney())
girl.die()
print(girl.isAlive())
#Task2 test
ada = Employee('Ada', 36, 3000, 'mathematician', 40)
print(ada.getJobTitle())
ada.work(8)
ada.receivePay()
print("$" + str(ada.getMoney()))
ada.setWage(100)
ada.work(8)
ada.receivePay()
print("$" + str(ada.getMoney()))
ada.die()
#Task3 test
bill = Programmer('Bill', 25, 1000, 50)
bill.work(3)
bill.receivePay()
print("$",str(bill.getMoney()))
bill.spendMoney(1000)
bill.spendMoney(2000)