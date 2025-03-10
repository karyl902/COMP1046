#Task1
class Card:
    def __init__(self, suit, value_str):
        self.suit = suit
        self.value_str = value_str

    def getSuit(self):
        return self.suit

    def getValueStr(self):
        return self.value_str

    def getValue(self):
        if self.value_str == 'ace':
            return 1
        elif self.value_str in ['jack', 'queen', 'king']:
            return 10
        else:
            return int(self.value_str)

    def toString(self):
        return self.value_str + ' of ' + self.suit

c1 = Card('hearts', 'ace')
print(c1.toString(), 'is worth', c1.getValue())

c2 = Card('spades', 'jack')
print(c2.toString(), 'is worth', c2.getValue())


