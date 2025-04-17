#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

class Car:
    def __init__(self, make:str, model:str, year:int,colour:str,rego:str) -> None:
        self.__make = make
        self.__model = model
        self.__year = year
        self.__colour = colour
        self.__rego = rego
        return
    def __str__(self) -> str:
        return self.car_str()
    
    
    @property
    def values(self) -> list:
        return [
            self.make, 
            self.model, 
            str(self.year), 
            self.colour, 
            self.rego
            ]
    def car_str(self) -> str:
        return " ".join(self.values)
    
    def csv_str(self) -> str:
        return ",".join(self.values)
    
    @property
    def make(self) -> str:
        return self.__make
    
    @make.setter
    def make(self,make:str):
        self.__make = make
        return
    
    @property
    def model(self) -> str:
        return self.__module__
    
    @model.setter
    def model(self,model:str):
        self.__module__ = model
        return
    @property
    def year(self) -> int:
        return self.__year
    
    @year.setter
    def year(self,year:int):
        self.__year = int(year)
        return
    
    @property
    def colour(self) -> str:
        return self.__colour
    
    @colour.setter
    def colour(self,colour:str):
        self.__colour = colour
        return
    
    @property
    def rego(self) -> str:
        return self.__rego
    
    @rego.setter
    def rego(self,rego:str):
        self.__rego = rego
        return
    
    @classmethod
    def create_from_input(cls):
        try:
            print("NEW CAR")
            make = input("Make: ")
            model = input("Model: ")
            year = int(input("Year: "))
            colour = input("Colour: ")
            rego = input("Rego: ")
            return Car(make,model,year,colour,rego)
        except Exception as e:
            raise e
    
    @classmethod
    def parse_csv_str(cls, csv_str:str):
        try:
            values = csv_str.split(",")
            values = [
                value.strip() for value in values
            ]
            make,model,year,colour,rego = values
            return cls(make,model,year,colour,rego)
        except Exception as e:
            raise e
    pass