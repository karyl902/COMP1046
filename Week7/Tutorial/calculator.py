#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
from operation import operation

class calculator:
    def __init__(self):
        self.__operation = []
        self.__home()
        pass

    def __history(self):
        if (len(self.__operation) > 0):
            print("history")
            for operation in self.__operations:
                print(operation)
                pass
            pass
        else:
            print("No history")
            pass
        self.__home()
        return
    
    def __add(self):
        print("Adding")
        self.__calculator("+")
        return
    
    def __subtract(self):
        print("Subtracting")
        self.__calculator("-")
        return
    
    def __multiply(self):
        print("Multiplying")
        self.__calculator("x")
        return
    def __divide(self):
        print("Dividing")
        self.__calculator("/")
        return
    def __operation(self,first, operator, second):
        try:
            operation = operation(first, operator, second)
            print(operation)
            self.__operation.append(operation)
            pass
        except Exception as e:
            raise e
    def __calculator(self, operator):
        first = input("Enter first number: ")
        second = input("Enter second number: ")
        try:
            self.__operation(first,second,operator)
            pass
        except Exception as e:
            print(e)
            pass
        finally:
            self.__home()
            pass
        return
    def __close(self):
        print("Closing")
        return
    def __home(self):
        print("Calculator".upper())
        menu = [
            ("Add", self.__add),
            ("Subtract", self.__subtract),
            ("Multiply", self.__multiply),
            ("Divide", self.__divide),
            ("History", self.__history),
            ("Close", self.__close)
        ]
        for item in menu:
            index = menu.index(item) + 1
            print(index, item[0])
            pass
        response = input("Select an option: ")

        try:
            option = int(response)
            menu[option - 1][1]()
            pass
        except Exception as e:
            print(e)
            print("Wrong input,must be a number between 1",len(menu))
            self.__home()
            pass
        return
    pass
calculator()