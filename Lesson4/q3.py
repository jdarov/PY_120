class AnimalSoundException(Exception):

    def __init__(self, sound):
        if not isinstance(sound, str):
            message = f'{sound} is not a valid animal sound. Please enter a sound with letters'
        else:
            message = f'{sound} is not a recognized animal sound'

        super().__init__(message)


class Animal:
    
    @staticmethod
    def speak(sound):
        if not isinstance(sound, str):
            raise AnimalSoundException(sound)
        print(sound)

class Cat(Animal):

    def meow(self):
        self.speak('Meow')
    
class Dog(Animal):

    def bark(self):                                                                     
        self.speak('Woof Woof!')


dog = Dog()
dog.bark()

cat = Cat()
cat.meow() 