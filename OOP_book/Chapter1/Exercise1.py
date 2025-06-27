class Car:

    DEFAULT_SPEED = 0
    DISTANCE_TRAVELED = 0
    FUEL_BURNED = 0

    def __init__(self, model, model_year, color):
        self._model = model
        self._model_year = model_year
        self._color = None
        self.color = color
        self._speed = Car.DEFAULT_SPEED
    
    def engine_on(self):
        print(f'{self.car_name} engine is ON')
    def accelerate(self):
        self._speed += 30
        print(f'{self.car_name} has accelerated to {self._speed} MPH')
    def brake(self):
        self._speed = max(0, self._speed-10)
        print(f'{self.car_name} is braking and now going {self._speed} MPH')
    def engine_off(self):
        print(f'{self.car_name} engine is OFF')
    @property
    def car_name(self):
        return f'{self._model_year} {self.color} {self._model}'
    @property
    def model(self):
        return self._model
    @property
    def model_year(self):
        return self._model_year
    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, value):
        if value <= 0:
            raise ValueError('Speed must be positive or you are go backwards in time')
        self._speed = value
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, new_color):
        if not isinstance(new_color, str):
            raise ValueError('Color must be a word')
        self._color = new_color
    @staticmethod
    def spray_color_of_car(spray_color):
        print(f'The new paint job {spray_color} looks great!')
    @staticmethod
    def gas_mileage(miles_driven=100, fuel_burned=5):
        return miles_driven/fuel_burned
    
    def __str__(self):
        return self.car_name

ferrari = Car('ferrari', 2025, 'red')
ferrari.engine_on()
ferrari.accelerate()
for i in range(3):
    ferrari.brake()
ferrari.engine_off()

print(ferrari.color)
ferrari.color = 'blue'
print(ferrari.color)

print(ferrari.model)
print(ferrari.model_year)

ferrari.spray_color_of_car('green')

print(ferrari.gas_mileage())

corvette = Car('corvette', 2011, 'blue')
print(corvette.gas_mileage(120, 2))

print(ferrari)
ferrari.color = 'red'
print(ferrari)