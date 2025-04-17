#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

from ui import *
from car import *
import os
class App:
    __filename = "cars.csv"
    def __init__(self) -> None:
        self.__cars = list()
        self.__load()
        self.__home()
        
        return
    def __home(self):
        name = "Car Fleet Home Menu"
        options= [
            MenuItem("New Car", self.__purchase),
            MenuItem("View Fleet", self.__view_fleet),
            MenuItem("Save to file", self.__save),
        ]
        Menu(name, options)
        return
    def __load(self):
        
        try:
            filename = self.__filename
            folder = os.getcwd()
            filepath = os.path.join(folder, filename)
            print(filepath)
            with open(filepath, "r") as file:
                lines = file.readlines()
                for line in lines:
                    try:
                        car = Car.parse_csv_str(line.strip())
                        print(car)
                        print(line)
                        self.__cars.append(car)
                        pass
                    except Exception as e:
                        pass
                    pass
                pass
            pass
        except Exception as e:
            pass
        return
        
    def __save(self):
        try:
            filename = self.__filename
            folder = os.getcwd()
            filepath = os.path.join(folder, filename)
            with open(filepath, "w") as file:
                file.writelines(car.csv_str() + "\n" for car in self.__cars)
                pass
        except Exception as e:
            pass
        return
    
    def __purchase(self):
        try:
            car = Car.create_from_input()
            self.__cars.append(car)
            print("Adding",car,"to fleet")
            self.__save()
            pass
        except Exception as e:
            print(e)
            pass
        finally:
            self.__home()
            pass
        return
    
    def __view_car(self,car: Car):
        car.display_details()
        self.__home()
        return
    
    def __view_fleet(self):
        name = "Fleet Menu"
        options = [
            MenuItem(car.car_str(), self.__view_car, [car]) for car in self.__cars
        ]
        options.append(MenuItem("Back", self.__home))
        Menu(name, options)
        return
    pass

    def __close(self):
        self.__save()
        print("Saving and Closing")
        return
    pass
App()