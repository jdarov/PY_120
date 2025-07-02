class Dog:

    def __init__(self, breed: str = None):
        self.breed = breed

    def get_breed(self):
        if hasattr(self, 'breed'):
            return self.breed

    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self, new_breed):
        if not isinstance(new_breed, str):
            raise TypeError("Breed must be a name")
        self._breed = new_breed

class Cat:

    def get_name(self):
        if not hasattr(self, 'name'):
            raise TypeError("Name not set!")
        return self.name

golden = Dog('Golden Retriever')
poodle = Dog('Poodle')

kitty = Cat()

print(golden.breed)
print(poodle.breed)

print(golden.get_breed())
print(poodle.get_breed())

poodle.breed = 'cutie'
print(poodle.breed)