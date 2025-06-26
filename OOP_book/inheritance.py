class Pet:
    
    def __init__(self, name):
        self.name = name
        type_name = type(self).__name__
        print(f'I am {name}, a {type_name}')

    def eat(self):
        print(f'{self.name}: Yum-yum-yum')

class Dog(Pet):

    def speak(self):
        print(f'{self.name} says Woof!')
    
    def roll_over(self):
        print(f'{self.name} is rolling over')

class Cat(Pet):

    def speak(self):
        print(f'{self.name} says Meow!')

class Parrot(Pet):
    
    def speak(self):
        print(f'{self.name} wants a cracker!')

sparky = Dog('Sparky')
kitty = Cat('Kitty')
polly = Parrot('Polly')

for pet in [sparky, kitty, polly]:
    pet.speak()
    pet.eat()
