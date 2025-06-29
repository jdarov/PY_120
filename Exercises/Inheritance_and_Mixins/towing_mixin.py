class TowingMixIn:
    def tow(self):
        return "I can tow a trailer!"

class Vehicle(TowingMixIn):
    def __init__(self, year):
        self.year = year

class Truck(Vehicle):
    pass

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994
print(truck1.tow())           # I can tow a trailer!

car1 = Car(2006)
print(car1.year)              # 2006