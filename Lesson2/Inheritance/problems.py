class AnimalMixIn:

    def speak(self):
        return 'bark'
    def sleep(self):
        return 'sleeping'
    def run(self):
        return 'running!'
    def jump(self):
        return 'jumping!'

class Dog(AnimalMixIn):

    def fetch(self):
        return 'fetching!'

class Cat(AnimalMixIn):
    pass

class Bulldog(Dog):

    def sleep(self):
        return "snoring!"

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!
bull = Bulldog()
print(bull.sleep())