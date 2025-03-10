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
#Task2
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        self.cards = []
        for suit in suits:
            for value in values:
                new_card = Card(suit, value) 
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards) 

    def drawCard(self):
        if len(self.cards) > 0:
            return self.cards.pop() 
        else:
            print("Deck is empty")
            return None
class Hand:
    def __init__(self):
        self.cards = [] 

    def addToHand(self, card):
        if len(self.cards) < 5:
            self.cards.append(card) 
        else:
            print("Hand is full. Cannot add more cards.")

    def getHandValue(self):
        total = 0
        for card in self.cards:
            total += card.getValue() 
        return total

    def emptyHand(self):
        self.cards = [] 

    def showCards(self):
        output = ""
        for i in range(len(self.cards)):
            output += self.cards[i].toString()
            if i != len(self.cards) - 1:
                output += ", "
        print(output) 
