#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

colour_set = {
    "red",
    "green",
    "blue",
    "yellow",
    "cyan",
    "magenta",
    "black",
    "white"
}
print("Unsortred set")
print(colour_set)

#connect set to list
colour_list = list(colour_set)

print("Set as list")
print(colour_list)

#sort colour list
colour_list.sort()
print("Sorted List")
print(colour_list)

#use list comprehension 
colour_list_a = [colour for colour in colour_set]
print("List comprehension")
print(colour_list_a)

colour_list_b = list()
for colour in colour_set:
    colour_list_a.append(colour)
    colour_list_b.append(colour)
    colour_set.add(colour)
    pass

print("Comparing adding to list vs adding to set")
print(colour_set)
print(colour_list)
print()
#using set comprehension
colour_set_a = {colour for colour in colour_list}
print(colour_set_a)
print(colour_set)
print()
#list using list(set)
colour_list_c = set(colour_set_a)
print(colour_list_c)
print()
#set using set(list)
colour_set_b = set(colour_list)
print(colour_set_b)
print()


