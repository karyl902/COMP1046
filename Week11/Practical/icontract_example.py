#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
import icontract

@icontract.require(lambda x,y: (x > 4) and (y > 3))
@icontract.ensure(lambda result: result > 10)
def f(x,y):
    print(x+y)
    return x+y

f(5,4)
