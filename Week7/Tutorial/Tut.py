#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
try:    
    filename = "myfile.txt" 
    file = open(filename, "r") 
    lines = file.readlines()
    for line in lines:
        print(line)
        pass
    pass
except FileNotFoundError as e:
    print("File Not Found")
    print(e) 
    print(e.args)
    pass

except Exception as e:
    print(e)
    pass
else:
    print("No exceptions raised")
    pass
finally:
    print("end of File Exception Handling")
    print()
    pass
try:
    items = [2, 4, 11] 
    item = items[5] 
    print("Item:", item)
    pass

except Exception as e:
    print(e)
    pass

else:
    print("No exceptions raised")

finally:
    print("End of Index Out Of Range Exception Handling")
    print()
# index out of range exception handling
try:
    nums = [1, 2, 3]
    num = nums[10]
except Exception as e:
    print(e)
    print(e.args)
else:
    print("No exceptions raised")
finally:
    print("end, of index out of range exception handling")
    print()
try:
    d = 10
    n = 5
    a = n/4
    print("answer:", d,"/", n,"=", a)
    pass
except TypeError as e:
    print("Division requires a numbers")
    pass
except ZeroDivisionError as e:
    print("cannot divide by zero")
    pass
except Exception as e:
    print(e)
    print(e.args)
    pass
else:
    print("No exceptions raised")
    pass
finally:
    print("End, of Index out of range exception handling")
    print()
    pass
try:
    num = "ten"
    num = int(num)
    print("Number:", num)
    pass
except ValueError as e:
    print(e)
    print(e.args)
    pass
else:
    print("No exceptions raised")
    pass
finally:
    print("End, of value error exception handling")
    print()
    pass

# key value exception
try:
    dictionary = {
        4: "four",
        3: "three"
    }
    key = 10
    #key = 10
    #value = dictionary[key]
    value = dictionary.get[key]
    print("value:", value)
    pass
except Exception as e:
    print(e)
    print(e.args)
    pass
else:
    print("No exceptions raised")
    pass

finally:
    print("End, of key value exception handling")
    print()
    pass
# Number input exception handling
try:
    user = input("Please enter a number: ")
    num = float(user)
    print("Number:", 0)
    pass
except Exception as e:
    print(e)
    print(e.args)
    pass
else:
    print("No exceptions raised")
    pass
finally:
    print("end of number input exception handling")
    print()
    pass


