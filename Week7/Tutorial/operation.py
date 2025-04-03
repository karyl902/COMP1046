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
        self.answer = self.__calculate()
        pass

    def __str__(self) -> str:
        values = [
            str(self.first),
            self.operator,
            str(self.second),
            "=",
            str(self.result)
        ]
        return 
    def __operations(self):
        operations = {
            "+": self.__add,
            "-": self.__subtract,
            "x": self.__multiply,
            "/": self.__divide
        }
        return operations
    def __calculate(self):
        operator = self.operator
        try:
            operations = self.__operations
            operations[operator]()
            pass
        except Exception as e:
            return e
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
        return self.__second
    @property
    def operator(self):
        return self.__operator
    @property
    def result(self):
        return self.__answer
    @first.setter
    def second(self, first):
        try:
            self.__first = self.__convert_str_to_num(first)
        except Exception as e:
            raise e
    @second.setter
    def second(self, second):
        try:
            self.__second = self.__convert_str_to_num(second)
        except Exception as e:
            raise e
    @operator.setter
    def operator(self,operator):
        try:
            self.__operator = self.__convert_str_to_num(operator)
            pass
        except Exception as e:
            raise e
    @answer.setter
    def answer(self,answer):
        try:
            self.__answer = self.__convert_str_to_num(answer)
        except Exception as e:
            raise e