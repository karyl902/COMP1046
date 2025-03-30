#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
import vehicle
import combustion,electric,hybrid1,hybrid2
import battery,fueltank
vehicles = [
    vehicle.vehicle(combustion.CombustionEngine(),fueltank.FuelTank(60)),
    vehicle.vehicle(hybrid1.HybridEngine(),[fueltank.FuelTank(40),battery.Battery(240)]),
    vehicle.vehicle(hybrid1.HybridEngine(),[fueltank.FuelTank(50),battery.Battery(160)]),
    vehicle.vehicle(electric.ElectricEngine(),battery.Battery(300)),
]
for vehicle in vehicles:
    print(vehicle)