#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

class GameManager:
    task1 = None

    def __new__(cls):
        if cls.task1 is None:
            cls.task1 = super().__new__(cls)
        return cls.task1

    def __eq__(self, object):
        if id(self) == id(object):
            print("We are the same object because we have the same object ID!")
            return True
        else:
            print("We are not the same object!")
            return False


g1 = GameManager()
g2 = GameManager()
g1 == g2
    