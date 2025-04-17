#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

class MenuItem:
    def __init__(self, name:str, method,parameters=None) -> None:
        self.__name = name
        self.__method = method
        self.__parameters = parameters
        return
    @property
    def name(self) -> str:
        return self.__name
    @property
    def method(self) -> str:
        return self.__method
    @property
    def parameters(self) -> list:
        return self.__parameters
    pass
class Menu:
    def __init__(self, name:str, options: list) -> None:
        self.__name = name
        self.__options = options
        self.__run()
        pass
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def options(self) -> list:
        return self.__options
    def __run(self):
        print()
        print(self.name.upper())
        for option in self.options:
            index = self.options.index(option)
            index += 1
            name = option.name
            print(index, name)
            pass
        self.__input()
        return
    
    def __input(self):
        input_message = "Select Menu Option Number: "
        user_input = input(input_message)
        try:
            index = int(user_input) 
            index = index -1
            option = self.options[index]
            parameters = option.parameters
            if parameters is None:
                option.method()
                return
            else:
                if len(parameters) > 0:
                    option.method(*parameters)
                    return
        except Exception as e:
            print(e)
            input()
            self.__run()
            pass
        return
    pass