#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
from battery import Battery
from engine import Engine  
class ElectricEngine(Engine):
    def __init__(self, battery_capacity):
        super().__init__()
        self.battery = Battery(battery_capacity)  
    
    def start(self):
        if self.battery.level > 0:
            print("Electric engine started.")
        else:
            print("Battery level too low to start.")
    
    def charge_engine(self, amount):
        self.battery.charge(amount)  