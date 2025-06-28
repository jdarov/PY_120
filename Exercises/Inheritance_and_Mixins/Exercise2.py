from exercise3 import VehicleMixIn

class Vehicle(VehicleMixIn):

    _vehicles = 0

    def __init__(self):
        Vehicle._vehicles += 1
    
    @classmethod
    def vehicles(cls):
        return cls._vehicles

class Car(Vehicle):
    def __init__(self):
        super().__init__()

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
class Boat():
    def __init__(self):
        super().__init__()


print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
boat1 = Boat()

car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off


print(Boat.mro())
print(Car.mro())