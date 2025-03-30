#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
from engine import Engine
from electric import ElectricEngine
from combustion import CombustionEngine

class HybridEngine(Engine):
    def __init__(self):
        super().__init__()
        self.__electric_engine = ElectricEngine()
        self.__combustion_engine = CombustionEngine()
        pass
    @property
    def electric_engine(self):
        return self.__electric_engine
    @property
    def combustion_engine(self):
        return self.__combustion_engine
    def start(self):
        #T0D0 logic of deciding which engine to start
        return super().start()
    def stop(self):
        #T0D0 get the engine that is running and make sure both are stopped
        return super().stop()
    pass