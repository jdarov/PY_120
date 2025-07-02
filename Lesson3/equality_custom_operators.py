import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    @circumference.setter
    def circumference(self, circumference):
        self.radius = circumference / (2 * math.pi)

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @area.setter
    def area(self, area):
        self.radius = math.sqrt(area / math.pi)

    def print(self):
        print(f'{self.radius=}')
        print(f'{self.diameter=}')
        print(f'{self.circumference=}')
        print(f'{self.area=}')
        print()

circle = Circle(10)
circle.print()
# self.radius=10
# self.diameter=20
# self.circumference=62.83185307179586
# self.area=314.1592653589793

circle.radius = 5
circle.print()
# self.radius=5
# self.diameter=10
# self.circumference=31.41592653589793
# self.area=78.53981633974483

circle.diameter = 15
circle.print()
# self.radius=7.5
# self.diameter=15.0
# self.circumference=47.12388980384689
# self.area=176.71458676442586

circle.circumference = 30
circle.print()
# self.radius=4.7746482927568605
# self.diameter=9.549296585513721
# self.circumference=30.0
# self.area=71.61972439135292

circle.area = 50
circle.print()
# self.radius=3.989422804014327
# self.diameter=7.978845608028654
# self.circumference=25.066282746310005
# self.area=50.0