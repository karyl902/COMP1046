#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

class Inventory:
    def __init__(self):
        self.__oberservers = list()
        self.__product = None
        self.quantity = 0
        return

    def attach(self,observer):
        self.__oberservers.append(observer)
        return
    
    @property
    def product(self):
        return self.__product
    
    @product.setter
    def product(self,value):
        self.__product = value
        self.__update_observers()
        return
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantiry(self,value):
        self.__quantity = value
        self.__update_observers()
        


    def __update_observers(self):
        for observer in self.__oberservers:
            observer()
            pass
        return
    pass

class consoleObserver:
    pass
   