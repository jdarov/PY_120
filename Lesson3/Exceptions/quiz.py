class Point:
    def __init__(self, x, y):
        self.coordinates = {'x': x, 'y': y}

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return self.coordinates == other.coordinates
    def __str__(self):
        return f'{self.coordinates}'

point1 = Point(5, 10)
point2 = Point(5, 10)
point3 = point1
point1.coordinates['x'] = 4

print(point3 is point1)