#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

class CapitalIterable:
    def __init__(self, string):
        self.string = string
        pass

    def __iter__(self):
        return CapitalIterator(self.string)
    pass
class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0
    pass

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word
    
    def __iter__(self):
        return self
    pass

    def __str__(self):
        return " ".join(self.words)

sentences = [
    "the quick brown fox jumps over the lazy dog",
    "she sells seashells by the seashore",
    "the rain in Spain stays mainly in the plain",
]

# using generator and comprehension
sentences = (
    CapitalIterable(sentence) for sentence in sentences
)

for sentence in sentences:
    print(sentence)
    pass
