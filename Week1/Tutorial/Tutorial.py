class Calculator:
    def __init__(self) -> None:
        self.__history = [] 
        self.__home()
        return

    def history(self) -> None:

        if len(self.__history) > 0:
            for operation in self.__history:
                print(operation)
        else:
            print("No history")
        self.__home()
        return

    def __home(self) -> None:

        print("Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. History")
        print("6. Close")
        response = input("Please enter an option: ")
        # Exception handling
        try:
            option = int(response)
            if 1 <= option <= 6:
                options = [
                    self.add,
                    self.subtract,
                    self.multiply,
                    self.divide,
                    self.history,
                    self.close
                ]
                options[option - 1]() # Call the selected method
            else:
                print("Wrong input, must be a number between 1 and 6")
                self.__home()
        except ValueError:
            print("Wrong input, must be a number between 1 and 6")
            self.__home()

    def add(self) -> None:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            operation = f"{num1} + {num2} = {result}"
            print(operation)
            self.__history.append(operation)
        except ValueError:
            print("Invalid input. Please enter numbers.")
        self.__home()

    def subtract(self) -> None:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            operation = f"{num1} - {num2} = {result}"
            print(operation)
            self.__history.append(operation)
        except ValueError:
            print("Invalid input. Please enter numbers.")
        self.__home()

    def multiply(self) -> None:
 
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            operation = f"{num1} * {num2} = {result}"
            print(operation)
            self.__history.append(operation)
        except ValueError:
            print("Invalid input. Please enter numbers.")
        self.__home()

    def divide(self) -> None:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                operation = f"{num1} / {num2} = {result}"
                print(operation)
                self.__history.append(operation)
        except ValueError:
            print("Invalid input. Please enter numbers.")
        self.__home()

    def close(self) -> None:

        print("Closing calculator. Goodbye!")
        return


if __name__ == "__main__":
    calc = Calculator()
