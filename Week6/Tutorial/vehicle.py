#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
import fuelstorage
import engine

class vehicle:
    def __init__(self,engine:engine.Engine,fuel_storage:list):
        self.__engine = engine
        self.__fuel_storage = list()
        if isinstance(fuel_storage,fuelstorage.FuelStorage):
            self.__fuel_storage.append(fuel_storage)
            pass
        elif isinstance(fuel_storage,list):
            for fuel in fuel_storage:
                if isinstance(fuel,fuelstorage.FuelStorage):
                    self.__fuel_storage.append(fuel)
                    pass
                pass
            pass
        pass
    pass