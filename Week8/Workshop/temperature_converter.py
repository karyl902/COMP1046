#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity


def f_to_c(f):
    '''Convert argument temperature from fahrenheit to celsius.'''
    if (isinstance(f, int) or isinstance(f, float)):
        return (f-32)*(5/9)
    else:
        raise TypeError("Only int or float is allowed.")

def c_to_f(c):
    if (isinstance(c, int) or isinstance(c, float)):
        return (9 / 5) * c + 32
    else:
        raise TypeError("Only int or float is allowed.")