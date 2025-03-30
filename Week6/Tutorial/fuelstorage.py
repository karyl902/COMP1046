#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
import abc
class fuelstorage(metaclass=abc.ABCMeta):
    #should be abstract class
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__level = 0
        pass

    @property
    def level(self):
        return self.__level
    @property
    def capacity(self):
        return self.__capacity
    @property
    def percentage(self):
        return 100*self.__level/self.__capacity
    def __change_fuel_level(self,amount:float):
        new_level = self.__level + amount
        if new_level < 0:
            self.__level = 0
            pass
        elif new_level > self.__capacity:
            new_level = self.__capacity
            pass
        self.__level = new_level
        return self.__level
    def _increase_fuel(self, amount:float):
        self.__change_fuel_level(amount)
        return self.__level
    def _decrease_fuel(self, amount:float):
        self.__change_fuel_level(-amount)
        return self.__level
    pass