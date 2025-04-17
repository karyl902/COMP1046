#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

import unittest
from car import Car

class TestCar(unittest.TestCase):
    def test_car_year(self):
        Car("Ford","Falcon",1991,"red","ASD234")
        return
    def test_car_make(self):
        Car("Ford","Falcon","-19.92df","red","ASD234")
        return
    pass

unittest.main()