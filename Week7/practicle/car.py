#Task 1.2
class Car:
    def __init__(self, topSpeed):
        self.setTopSpeed(topSpeed)
        self.speed = 0

    def setTopSpeed(self, topSpeed):
        if topSpeed > 0:
            self.topSpeed = topSpeed
        else:
            raise Exception("Invalid top speed: " + str(topSpeed))

    def getTopSpeed(self):
        return self.topSpeed

    def getSpeed(self):
        return self.speed

    def accelerate(self):
        if self.speed + 10 > self.topSpeed:
            self.speed = self.topSpeed
            raise Exception(" Cannot accelerate above top speed: " + str(self.topSpeed))
        self.speed += 10

    def decelerate(self):
        if self.speed - 10 < 0:
            self.speed = 0
            raise Exception("Cannot decelerate below 0")
        self.speed -= 10

    def __str__(self):
        return " Car going " + str(self.speed) + "/" + str(self.topSpeed) + " kmph"


# Task 3.1
class SpeedException(Exception):
    pass


# Task 3.2
class NoDriverException(Exception):
    def __init__(self):
        super().__init__("Cannot drive without a Driver")


class Car:
    def __init__(self, topSpeed):
        self.setTopSpeed(topSpeed)
        self.speed = 0
        self.__driver = None

    def setTopSpeed(self, topSpeed):
        if topSpeed > 0:
            self.topSpeed = topSpeed
        else:
            raise SpeedException("Invalid top speed: " + str(topSpeed))

    def getTopSpeed(self):
        return self.topSpeed

    def getSpeed(self):
        return self.speed

    def accelerate(self):
        if self.__driver is None:
            raise NoDriverException()
        if self.speed + 10 > self.topSpeed:
            self.speed = self.topSpeed
            raise SpeedException("Cannot accelerate above top speed: " + str(self.topSpeed))
        self.speed += 10

    def decelerate(self):
        if self.__driver is None:
            raise NoDriverException()
        if self.speed - 10 < 0:
            self.speed = 0
            raise SpeedException("Cannot decelerate below zero")
        self.speed -= 10

    def setDriver(self, driver):
        self.__driver = driver

    def __str__(self):
        return "Car going " + str(self.speed) + "/" + str(self.topSpeed) + " kmph"

    

    