#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

unsorted_colour_dictionary = {
    "red": (1,0,0),
    "green": (0,1,0),
    "blue": (0,0,1),
    "yellow": (1,1,0),
    "cyan": (0,1,1),
    "magenta": (1,0,1),
    "black": (0,0,0),
    "white": (1,1,1)
}

print("Unsorted dictionary")
print(unsorted_colour_dictionary)
print()

#get all keys
keys = unsorted_colour_dictionary.keys()
#print(keys)
keys = list(keys)

print("keys")
print(keys)
print()

#sort keys
keys.sort()

print("Sorted keys")
print(keys)
print()

#create an empty dictionary
sorted_colour_dictionary = dict()

#loop through the keys
for key in keys:
    value = unsorted_colour_dictionary.get(key)
    #update the new dictionary 
    sorted_colour_dictionary.update({key: value})
    pass

print("Sorted dictionary")
print(sorted_colour_dictionary)
print()

#dictionary comprehension
sorted_colour_dictionary_a = {
    key: unsorted_colour_dictionary[key] for key in keys
}
print(sorted_colour_dictionary_a)
print()

#dictionary comprehension using kets ,values and items
unsorted_colour_dictionary_a = {
    key: unsorted_colour_dictionary[key] for key in keys
}
print(unsorted_colour_dictionary_a)
print()