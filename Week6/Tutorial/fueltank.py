#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
from fuelstorage import Fuelstorage
class FuelTank(Fuelstorage):
    def __init__(self, capacity):
        super().__init__(capacity)
        pass

    def refuel(self, amount):
        return self._increase_duel(amount)
    
    def use_fuel(self, amount):
        return self._decrease_fuel(amount)
    
    def drain_tank(self):
        return self._decrease_fuel(self.level)
    pass