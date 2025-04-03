#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
class operation:
    def __init__(self,first,operator,second):
        # T0D0 write properties
        self.first = first
        self.operator = operator
        self.second = second
        self.__calculator()
        pass

    def __str__(self) -> str:
        values = [
            str(self.first),
            self.operator,
            str(self.second),
            "=",
            str(self.result)
        ]
        pass
    def __calculate(self):
        return
    pass

    def __multiply(self):
        self.answer = self.first * self.second
        return
    def __divide(self):
        try:
            self.answer = self.first / self.second
            pass
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero")
        return
    def __convert_str_to_num(Self,number):
        try:
            number = float(number)
            if number.is_integer():
                number = int(number)
                pass
            return number
        except Exception:
            raise Exception("Must be a number")
    @property
    def first(self):
        return self.__first
    @property
    def second(self):
        return
    pass
