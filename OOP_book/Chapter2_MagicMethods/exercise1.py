class Car:

    def __init__(self, ID, car_year, car_color):
        self._ID = ID
        self._car_year = car_year
        self._car_color = car_color

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({repr(self._ID)}, {repr(self._car_year)}, {repr(self._car_color)})'
    def __str__(self):
        return f'{self._car_color} {self._car_year} {self._ID}'

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')