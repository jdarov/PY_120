class Pet:
    def __init__(self, name='kitty'):
        self._name = name

    def play(self):
        print('I am playing')

class Predator:

    def __init__(self, name="predator"):
        self._name = name

    def play(self):
        print('I am hunting')

class Cat(Predator, Pet):

    def purr(self):
        print('I am purring')

cat = Cat()
cat.purr()          # I am purring
cat.play()          # I am playing
print(cat._name)