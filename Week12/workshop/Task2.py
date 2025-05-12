#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
class Base: 
 
    def printMe(self): 
        print("Calling method printMe() in class Base.") 
 
class Left(Base): 
 
    def printMe(self): 
        print("Calling method printMe() in class Left.") 
        super().printMe() 
 
class Right(Base): 
 
    def printMe(self): 
        print("Calling method printMe() in class Right.") 
        super().printMe() 

 
class Sub(Left,Right): 
 
    def printMe(self): 
        print("Calling method printMe() in class Sub.") 
        super().printMe() 
 
s = Sub() 
s.printMe() 

# 1 Calling method printMe() in class Sub.
#   Calling method printMe() in class Left.
#   Calling method printMe() in class Right.
#   Calling method printMe() in class Base.


# 2 Reason: In the original code, the printMe method of each class prints its own information first and then calls super().printme (), printing in the MRO order Sub -> Left -> Right -> Base to form the original output sequence.

# 3
class Sub(Right, Left):  
    def printMe(self):  
        print("Calling method printMe() in class Sub.")  
        super().printMe()  

# 4 
class Base:
    def printMe(self):
        print("Calling method printMe() in class Base.")


class Left(Base):
    def printMe(self):
        super().printMe()
        print("Calling method printMe() in class Left.")


class Right(Base):
    def printMe(self):
        super().printMe()
        print("Calling method printMe() in class Right.")


class Sub(Right, Left):
    def printMe(self):
        super().printMe()
        print("Calling method printMe() in class Sub.")


s = Sub()
s.printMe()



# 5 Calling method printMe() in class Base.
#   Calling method printMe() in class Left.
#   Calling method printMe() in class Right.
#   Calling method printMe() in class Sub.  

#6 Reason: After modifying the code, each class first calls super().printme (). This will execute the printMe method starting from the top-level parent class in the new MRO order: Sub -> Right -> Left -> Base. After completing the printing of the parent class, it will return layer by layer to execute the printing of the child class. So the output sequence is the opposite of the original code.
