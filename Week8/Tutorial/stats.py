#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
class Stats:
    def __init__(self, numbers = list()) -> None:
        self.numbers = numbers
        pass
    @property
    def numbers(self):
        return self.__numbers
    @numbers.setter
    def numbers(self, numbers):
        self.__numbers = numbers
        return
    @property
    def len(self):
        return len(self.numbers)
    @property
    def sum(self):
        return sum(self.numbers)
    @property
    def min(self):
        return min(self.numbers)
    @property
    def max(self):
        return max(self.numbers)
    @property
    def mean(self):
        return self.sum / self.len
    @property
    def midpoint(self):
        return (self.min + self.max) / 2
    @property
    def median(self):
        self.numbers.sort()
        index = round(self.len / 2)
        if self.len % 2 == 0:
            return (self.numbers[index] + self.numbers[index - 1]) / 2
        else:
            return self.numbers[index-1]
    def add(self, number):
        self.numbers.append(number)
        return
    def remove(self, number):
        self.numbers.remove(number)
        return
    pass

stats = Stats([1, 2, 3, 4, 5])
print(stats.numbers)
print("Length:",stats.len)
print("Sum:",stats.sum)
print("Min:",stats.min)
print("Max:",stats.max)
print("Mean:",stats.mean)
print("Midpoint:",stats.midpoint)
print("Median:",stats.median)
print(stats.numbers)