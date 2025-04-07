from car import Car
# Task 3.2
car1 = Car(250)
car1.setDriver("Valentino")
# 1
car1 = Car(250)
print("Step 1: ")
print(car1)

# 2 & 3
print("Step 2 & 3:")
try:
    car2 = Car(-99)
    print(car2)
except Exception as e:
    print(e)

# 4 & 5
print("Step 4 & 5:")
try:
    for _ in range(30):
        car1.accelerate()
        print(car1)
except Exception as e:
    print(e)
    # 6 & 7
    print("Step 6 & 7:")
    for _ in range(30):
        try:
            car1.decelerate()
            print(car1)
        except Exception as e:
            print(e)

# 8
print("Step 8:")
while True:
    try:
        user_input = input("Please enter a float as the top speed: ")
        speed = float(user_input)
        car1.setTopSpeed(speed)
        break
    except ValueError as e:
        print(e)
    
