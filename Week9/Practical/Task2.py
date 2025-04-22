#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
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
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif month in {4, 6, 9, 11}:
            return 30
        elif cls.isLeapYear(year):
            return 29
        else:
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

    def __init__(self, day, month, year):
        if not self.isValidYear(year):
            raise Exception("Invalid year: %s. Year must be an integer." % year)
        if not self.isValidMonth(month):
            raise Exception("Invalid month: %s. Month must be 1 - 12." % month)
        if not self.isValidDay(day, month, year):
            max_day = self.getDaysInMonth(month, year)
            raise Exception("Invalid day: %s. Day must be 1 - %s." % (day, max_day))
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        month_name = self.getMonthName(self.month)
        return "%s %s, %s" % (self.day, month_name, self.year)

    def __lt__(self, other):
        if not isinstance(other, Date):
            return False  
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                return self.day < other.day
        return False
    
d1 = Date(18, 2, 2020) 
d2 = Date(3, 3, 2020) 
if d1 < d2: 
    print(d1, 'is less than', d2) 
elif d2 < d1: 
    print(d1, 'is more than', d2) 
else: 
    print(d1, 'is equal to', d2) 