class Vehicle:
    def __init__(self):
        pass
    def __str__(self):
        return "vehicle"
    def __name__(self):
        return self.__str__()
    def start_engine(self):
        print("start engine")
        return
    def stop_engine(self):
        print("stop engine")
        return
    def move_forward(self):
        print("move forward")
        return
    def move_back(self):
        print("move back")
        return
    def turn_left(self):
        print("turn left")
        return
    def turn_right(self):
        print("turn right")
        return
    def accelerate(self):
        print("accelerate")
        return
    def decelerate(self):
        print("decelerate")
        return
    pass  