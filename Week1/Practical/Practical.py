#1

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
total = sum(len(day) for day in week)
num = len(week)
length = total/ num
print("Days of the week:", week)
print("Total number of letters:", total)
print("Number of words:", num)
print("Average length of words:", length)

#2
def distance(velocity, time):
    return velocity * time

result = distance(60, 100)
print("Distance travelled:",result,"metres")

#3
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

#Test
test = kinetic_energy(10, 60)
print("Kinetic Energy:",test,"joules")

#4
class MovingObject:
    def __init__(self, velocity, mass):
        self.velocity = velocity  
        self.mass = mass         

    def distance(self, duration):
        return self.velocity * duration

    def kinetic_energy(self):
        return 0.5 * self.mass * self.velocity ** 2
moving_obj = MovingObject(velocity=60, mass=10)
print("Distance travelled:", moving_obj.distance(100), "metres")
print("Kinetic Energy:", moving_obj.kinetic_energy(), "joules")


#5
class MovingObject:
    def __init__(self, velocity, mass):
        self.velocity = velocity  
        self.mass = mass       

    def distance(self, duration):
        return self.velocity * duration

    def kinetic_energy(self):
        return 0.5 * self.mass * self.velocity ** 2


teest = MovingObject(velocity=6, mass=20)


dis_travelled = teest.distance(60)
print("Distance travelled:", dis_travelled, "meters")

kinetic_energy = teest.kinetic_energy()
print("Kinetic Energy:", kinetic_energy, "joules")
