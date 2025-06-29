class Vehicle:

    def __init__(self, make, model):
        self._make = make
        self._model = model

    def get_wheels(self):
        return 4
    
    def info(self):
        return f'{self._make} {self._model}'

class Car(Vehicle):

    pass

class Motorcycle(Vehicle):

    def get_wheels(self):
        return 2

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self._payload = payload

    def get_wheels(self):
        return 6
    
