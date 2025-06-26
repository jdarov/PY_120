class Animal:

    def __init__(self, name):
        self.name = name
    
    def show_animal(self):
        print(f'This animal is a {type(self).__name__}')
    
    def print_name(self):
        print(f'My name is {self.name}')

class Lion(Animal):
    pass
class ClownFish(Animal):
    pass

mufasa = Lion('Mufasa')
nemo = ClownFish('Nemo')

for animal in [mufasa, nemo]:
    animal.show_animal()
    animal.print_name()