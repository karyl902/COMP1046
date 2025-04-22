#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
class Person: 
    __population = 0 
 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
        Person.__population += 1 
     
    def __str__(self): 
        return self.name + ' is ' + str(self.age) + ' years old' 
     
    @classmethod 
    def get_population(cls): 
        return cls.__population 
 
    @classmethod 
    def input(cls): 
        name = input('Enter the name: ') 
        age = int(input('Enter the age: ')) 
        return cls(name, age)



print('Currently', Person.get_population(), 'people') 
 
you = Person.input() 
print('Now', Person.get_population(), 'person') 
 
actor = Person("Ernie Dingo", 64) 
 
print(actor) 
print(you) 
print('Now', Person.get_population(), 'people')

#Task1.1

class Date:
    monthNames = ["January", "February", "March", "April",
                  "May", "June", "July", "August",
                  "September", "October", "November", "December"]

    @classmethod
    def getMonthName(cls, number):
        if 1 <= number <= 12:
            return cls.monthNames[number - 1]
        raise ValueError("Invalid month number")

    @classmethod
    def getDaysInMonth(cls, month, year=1):
        if not cls.isValidMonth(month):
            raise ValueError("Invalid month")
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif month in {4, 6, 9, 11}:
            return 30
        elif cls.isLeapYear(year):
            return 29
        return 28

    @classmethod
    def isLeapYear(cls, year):
        return isinstance(year, int) and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

    @classmethod
    def isValidYear(cls, year):
        return isinstance(year, int)

    @classmethod
    def isValidMonth(cls, month):
        return isinstance(month, int) and 1 <= month <= 12

    @classmethod
    def isValidDay(cls, day, month, year):
        if not isinstance(day, int) or day < 1:
            return False
        max_day = cls.getDaysInMonth(month, year)
        return day <= max_day

   

print("Testing class methods:")
print(Date.getMonthName(1))
print(Date.getMonthName(6))
print(Date.getMonthName(12))
print(Date.getDaysInMonth(3))
print(Date.getDaysInMonth(2, 2020))
print(Date.getDaysInMonth(2, 2021))
print(Date.isValidYear(2023))
print(Date.isValidYear("2023"))
print(Date.isValidMonth(0))
print(Date.isValidDay(30, 4, 2023))
print(Date.isValidDay(31, 4, 2023))
