#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
import abc
class Engine(metaclass = abc.ABCMeta):
    #should be abstract class
    def __init__(self):
        self.__is_running = False
        self.__speed = 0
        pass
    @abc.abstractmethod
    def start(self):
        self.__is_running = True
        return
    @abc.abstractmethod
    def stop(self):
        self.__is_running = False
        return
    pass