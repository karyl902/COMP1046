from vehicle import Vehicle # type: ignore
from aircraft import Aircraft  # type: ignore

#vehicle
#print("vehicle")
print(Vehicle.name())
vehicle = Vehicle()
vehicle.start_engine()
vehicle.move_back()
vehicle.turn_left()
vehicle.move_forward()
vehicle.accelerate()
#can call any of the cehicle methods
print()

#aircraft
#print("aircraft")
aircraft = Aircraft()
#print(aircraft.name)
print(aircraft.name)
aircraft.start_engine()
aircraft.move_back()
aircraft.turn_right()
aircraft.move_forward()
aircraft.turn_left()
aircraft.accelerate()
aircraft.move_up()
print("aircraft is in the air")
# can call any of the aircraft methods
# can call any of the vehicle methods