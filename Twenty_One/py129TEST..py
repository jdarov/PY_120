class Protected:

    __CONSTANT = 100
    _CONSTANT = 200
    def __init__(self, name, color):
        self.name = name
        self.__color = color

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise TypeError("Name must be a string")
        
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError("Color must be a name of a color")
        self.__color = new_color
    



protected = Protected('John', 'Red')

print(protected.name)

protected.name = "Josh"
# protected.name = 1 #TypeError
print(protected.name)

print(protected.color)
protected.__color = "orange"
print(protected.color)
protected.color = 'orange'
print(protected.color)