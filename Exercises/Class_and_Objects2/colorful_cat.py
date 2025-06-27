class Cat:
    CAT_COLOR = 'purple'
    def __init__(self, name):
        self._name = name
    
    def greet(self):
        print(f"Hello! My name is {self._name} and I'm a {Cat.CAT_COLOR} cat!")

kitty = Cat("Sophie")
kitty.greet()