class SayMixIn:
    
    def says(self):
        
        return (f'{self.__class__.__name__} says hello and has {self._number_of_children} children' 
                if hasattr(self, '_number_of_children')
                else f'{self.__class__.__name__} says hello')

class Grandparent(SayMixIn):

    def __init__(self, name):
        self._name = name

    def says(self):
        return "I'm a grumpy grandpa"
    

class Parent(Grandparent):
    
    def __init__(self, name, number_of_children):
        super().__init__(name)
        self._number_of_children = number_of_children

    def says(self):
        return f"I am a Parent with {self._number_of_children} children!"
    
class Child(Parent):

    def __init__(self, name):
        super().__init__(name, 0)

    says = SayMixIn.says
    
grandparent = Grandparent("John")
parent = Parent("Mary", 2)
child = Child("Alex")

print(grandparent.says())
print(parent.says())
print(child.says())    