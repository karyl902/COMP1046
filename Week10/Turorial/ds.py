#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

#complete using tuples
#tubles can be converted to objects
#tubles can be converted to dictionaries

#create list of tuples
list_of_cars_as_tuples = [
    ("Ford", "Falcon", 1990, "red", "SDF234"),
    ("Holden", "Commodore", 1995, "white", "DFA342"),
    ("Toyota", "Corolla", 2008, "blue", "GER234"),
    ("Toyota", "Camry", 2014, "white", "HJC234"),
    ("Holden", "Cruze", 2013, "green", "HJC234"),
    ("Holden", "Astra", 2014, "red", "KJL239"),
    ("Ford", "Mustang", 1989, "blue", "KJL329"),
    ("Holden", "Commodore", 1998, "white", "MNJ436"),
    ("Ford", "Falcon", 1994, "white", "PJB829"),
    ("Ford", "Falcon", 1996, "white", "MMF204"),
    ("Toyota", "Corolla", 2009, "white", "MTY915"),
    ("Toyota", "Camry", 2013, "white", "KWN954"),
    ("Ford", "Mustang", 1989, "white", "HJC739"),
    ("Ford", "Laser", 1994, "red", "VCC929"),
    ("Holden", "Cruze", 2010, "white", "VGF789"),
    ("Holden", "Astra", 2013, "blue", "JKR567"),
    ("Holden", "Cruze", 2013, "purple", "KSP745")
]
#print(list_of_cars_as_dicts)
# print()

car_as_dict_keys = [
    "Make",
    "Model",
    "Year",
    "Colour",
    "Rego"
]
list_of_cars_as_dicts = [
    dict(zip(car_as_dict_keys, car_tuple)) for car_tuple in list_of_cars_as_tuples
] 
#print(list_of_cars_as_dicts)
# print()

# alternatively
list_of_cars_as_dicts_a = list()
for car_tuple in list_of_cars_as_tuples:
    car_zip = zip(car_as_dict_keys, car_tuple)
    # print(car_zip)
    car_dict = dict(car_zip)
    # print(car_dict)
    list_of_cars_as_dicts_a.append(car_dict)
    pass

# print(list_of_cars_as_dicts_a)
# print()

for car_tuple in list_of_cars_as_tuples:
    print(car_tuple)
    pass
print()

for car_dict in list_of_cars_as_dicts:
    print(car_dict)
    pass
print()

# get all the colour
print("COLOUR")

colour_list_using_car_tuples = [
    car[3] for car in list_of_cars_as_tuples
]
print(colour_list_using_car_tuples)

# alternative
colour_list_using_car_dicts = [
    car[3] for car in list_of_cars_as_dicts
]
print(colour_list_using_car_dicts)
print()

#convert colour list to sets
colour_set_using_cars_as_tuples = {
    car[3] for car in list_of_cars_as_tuples
}
print(colour_set_using_cars_as_tuples)

colour_set_using_cars_as_dicts = {
    car["Colour"] for car in list_of_cars_as_dicts
}
print(colour_set_using_cars_as_dicts)

# get all the registration numbers
print("REGO")

rego_list_using_cars_as_tuples = [
    car[4] for car in list_of_cars_as_tuples
]
print(rego_list_using_cars_as_tuples)

rego_list_using_cars_as_dicts = [
    car["rego"] for car in list_of_cars_as_dicts
]
print(rego_list_using_cars_as_dicts)
print()

rego_set_using_cars_as_tuples = {
    car[4] for car in list_of_cars_as_tuples
}
print(rego_set_using_cars_as_tuples)

rego_set_using_cars_as_dicts = {
    car.get("Rego") for car in list_of_cars_as_dicts
}
print(rego_set_using_cars_as_dicts)
print()

rego_list_count_tuple = len(rego_list_using_cars_as_tuples)
rego_list_count_dict = len(rego_list_using_cars_as_dicts)
rego_set_count_tuple = len(rego_set_using_cars_as_tuples)
rego_set_count_dict = len(rego_set_using_cars_as_dicts)

print("Set vs list Counts")
print("Dict", rego_set_count_dict, rego_list_count_dict, rego_set_count_dict == rego_list_count_dict)
print("Tuple", rego_set_count_tuple, rego_list_count_tuple, rego_set_count_tuple == rego_list_count_tuple)
print()

#using dictionaries to store a list of cars

car_dictionary_using_cars_as_tuples = {
    car[4]: car for car in list_of_cars_as_tuples
}


car_dictionary_using_cars_as_dicts = {
    car["Rego"]: car for car in list_of_cars_as_dicts
    #car.get("Rego"): car for car in list_of_cars_as_dicts
}

print("dictionary items")
for key, value in car_dictionary_using_cars_as_tuples.items():
    car = value
    print(key, " ".join([str(attribute) for attribute in car]))
    pass

print("dictionary keys")
for key in car_dictionary_using_cars_as_tuples.keys():
    print(key)
    pass

#get all the makes 
make_list = [
    car[0] for car in car_dictionary_using_cars_as_tuples
]

print(make_list)
make_set = {
    car["make"] for car in list_of_cars_as_dicts
}
print(make_set)
print()

# get all the makes and models
make_from_set = {
    make: list() for make in make_set
}
make_from_list = {
    make: list() for make in make_list
}

#the two dictionaries should look identical
#the reason being that the keys should by unique
#like values in a set
print(make_from_set)
print(make_from_list)
print()

#use the set of makes as keys 
makes = {
    make: list() for make in make_set
}

for key,value in makes.items():
    models = {
        car[1] for car in list_of_cars_as_tuples if car[0] == key
    }
    print(models)
    makes.update({key: models})
    pass
print(makes)
print()

print("MODELS")
#using dictionaries comprehension

models = {
    make: list({car[1] for car in list_of_cars_as_tuples if car[0] == make}) for make in make_set
}
print(models)
print()

print("YEARS")
year_list = [
    car[2] for car in list_of_cars_as_tuples
]
print(year_list)

year_set = {
    car["year"] for car in list_of_cars_as_dicts
}
print(year_set)
print()


#using a tuple as a key
year_dict = {
    (car[0], car[1]): list for car in list_of_cars_as_tuples
}

for key, value in year_dict.items():
    make = key[0]
    model = key[1]
    years = {
        car[2] for car in list_of_cars_as_tuples if car[0] == make and car[1] == model
    }
    year_dict.update({key: years})
    pass
print(year_dict)
print()

print("Set Methods")
print()

print("UNION")
all_years = set()
for key in year_dict.keys():
    all_years = all_years.union(value)
    pass

print(all_years)
print()

print("INTERSECT (or INTERSECTION)")
for key in year_dict.keys():
    interesect_set = all_years.intersection(value)
    value_set = value.intersection(all_years)
    print(value)
    print(interesect_set)
    print(value_set)
    print()
    pass

print("DIFFERENCE")
for key, value in year_dict.items():
    difference_set = all_years.difference(value)
    value_set = value.difference(all_years)
    print(value)
    print(difference_set)
    print(value_set)
    print()
    pass

print("SYMMETRIC DIFFERENCE")
for key, value in year_dict.items():
    symmetric_difference_set = all_years.symmetric_difference(value)
    value_set = value.symmetric_difference(all_years)
    print(value)
    print(symmetric_difference_set)
    print(value_set)
    print()
    pass

class Car:
    def __init__(self, make, model, year, colour, rego):
        self._make = make
        self._model = model
        self._year = year
        self._colour = colour
        self._rego = rego

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def colour(self):
        return self._colour

    @property
    def rego(self):
        return self._rego

    def __str__(self):
        return "Make: " + str(self._make) + ", Model: " + str(self._model) + ", Year: " + str(self._year) + ", Colour: " + str(self._colour) + ", Rego: " + str(self._rego)


#HOMEWORK
#make a car class
#make a version of this file using car objects instead of tuples and dictionaries
#remember to use properties and overwrite the __str__method
#make a uml of the car class