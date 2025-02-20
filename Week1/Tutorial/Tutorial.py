class Calculator:   
    def __init__(self):
        self.__calculations = []
        self.__home()
    
    def __home(self):
        print("CALCULATOR")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. History")
        print("6. Exit")
        
        response = input("Please enter an option: ")
        try:
            option = int(response)
            options = [
                self.__add,
                self.__subtract,
                self.__multiply,
                self.__divide,
                self.__history,
                self.__exit
            ]
            options[option - 1]()
        except (ValueError, IndexError):
            print("Invalid option. Please try again.")
            self.__home()
        pass
        except Exception as e:
        print("Exception:", e)
        print("Invalid option. Please try again.")
        self.__home()
        pass
    return
    