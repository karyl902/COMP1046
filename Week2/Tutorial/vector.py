class Vector:
    def __init__(self, x, y):
        self.x = x(x)
        self.y = y(y)
        return
    def set_(self,x):
        self.__x = x
        return
    def set_y(self,y):
        self.__y = y
        return
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def __validate(self, num) -> bool:
        if isinstance(num, int):
            return True
        if isinstance(num, float):
            return True
        return False
    pass
v = Vector(3,4)
print(v.get_x(),v.get_y())
