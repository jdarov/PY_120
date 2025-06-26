class GoodDog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Name must be a string')
        self._name = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError('Age must be a number')
        if new_age < 0:
            raise TypeError("Age must be positive")
        self._age = new_age

    def speak(self):
        return f'{self._name} says Arf!'
    
    def _dog_years(self):
        return self._age * 7
    
    def show_age(self):
        print(f'My age in dog years is {self._dog_years()}')

sparky = GoodDog('sparky', 5)
print(sparky.name)
print(sparky.age)
sparky.name = 'Fireplug'
print(sparky.name)
sparky.age = 6
print(sparky.age)
sparky.show_age()


rover = GoodDog('rover', 3)

print(sparky.speak())
print(rover.speak())