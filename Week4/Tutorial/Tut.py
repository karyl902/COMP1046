from vehicle import Vehicle  # type: ignore

class Aircraft(Vehicle):
    def __init__(self):
        super().__init__()
        pass
    def __str__(self):
        return "aircraft"
        #return super().__str__()
    #def __name__(self):
        #return super().name()
    def move_up(self):
        print("move up")
        return
    def move_down(self):
        print("move down")
        return
    
    pass 