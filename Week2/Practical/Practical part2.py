#Task 2
import turtle
import random

class TurtleCluster:
    def __init__(self):
        self.cluster = []
# Task 2.1
    def addTurtle(self,turtle):
         self.cluster.append(turtle)
#Task 2.2
    def goToLocation(self, x, y):
        for turtle in self.cluster:
            turtle.goto(x, y)
#Task 2.3
    def spreadOut(self):
        for turtle in self.cluster:
            bend = random.randint(1, 360)
            distance = random.randint(1, 100)
            turtle.right(bend)
            turtle.forward(distance)


#Task 2.4
win = turtle.Screen()
turtle1 = TurtleCluster()
for _ in range(5):
    tut = turtle.Turtle()
turtle1.addTurtle(tut)
turtle1.spreadOut()
turtle1.goToLocation(0,0)
turtle1.spreadOut()
win.exitonclick()


