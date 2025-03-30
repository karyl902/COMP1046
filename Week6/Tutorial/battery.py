#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
class Battery:
    def __init__(self, capacity):
        self._capacity = capacity
        self._level = 0.0
    
    @property
    def level(self):
        return self._level
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def percentage(self):
        return (self._level / self._capacity) * 100 if self._capacity != 0 else 0
    
    def charge(self, amount):
        self._level = min(self._level + amount, self._capacity)
    
    def discharge(self, amount):
        self._level = max(self._level - amount, 0)