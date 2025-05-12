#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

class NumbersIterable: 
    def __init__(self, numbers): 
        self.numbers = numbers
    def __iter__(self):
        self.index = 0 
        return self
    def __next__(self):
        if self.index >= len(self.numbers): 
            raise StopIteration 
        value = self.numbers[self.index]
        self.index += 1
        return int(value) 
 
niterable=NumbersIterable(["1", 2.0, "4",5,6.1,"7",8,9.2]) 
 
for i in niterable: 
    print(i) 