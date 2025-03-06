import random as rand
class Dice:
    def __init__ (self):
        self.__side = rand.randint(1,6)
        return
    def get_side(self):
        return self.__side
    def side_side(self,side):
        if side >= 1 and side <= 6:
            self.__side = side
            pass
        return
    def roll(self):
        self.set_side(self.__random_int())
        return self.__side
    pass

dice = Dice()
print(dice.get_side())
dice.side_side(4)
print(dice.get_side())
dice.side_side(10)
print(dice.get_side())
dice.roll()
print(dice.get_side())
