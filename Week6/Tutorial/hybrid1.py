#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
from combustion import CombustionEngine
from electric import ElectricEngine

class HybridEngine(CombustionEngine,ElectricEngine):
    def __init__(self):
        super().__init__()

        pass
    def start(self):
        #T0D0 logic of deciding which engine to start
        return super().start()
    def stop(self):
        #T0D0 get the engine that is running and make sure both are stopped
        return super().stop()
    pass