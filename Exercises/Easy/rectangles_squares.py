class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height
    
class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        
    @property
    def size(self):
        return self._width
    @size.setter
    def size(self, new_size):
        self._width = new_size
        self._height = new_size

    
square = Square(5)
print(square.area == 25)      # True

square.size = 10
print(square.area)