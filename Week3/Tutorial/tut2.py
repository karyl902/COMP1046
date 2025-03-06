import random as rand
class Dice:
    def __init__ (self):
        self.__side = rand.randint(1,6)
        return
    @property
    def side(self):
        return self.__side
    @side.setter

    def side_side(self,side):
        if side >= 1 and side <= 6:
            self.__side = side
            pass
        return
    def roll(self):
        self.__side = self.__random_int()
        return self.side
    pass

dice= Dice()
print(dice.side())
dice.side = 4
print(dice.side)
dice.side = 10
print(dice.side)
dice.roll()
print(dice.side)

