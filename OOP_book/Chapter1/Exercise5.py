class Person():

    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)
    
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
    @name.setter
    def name(self, names):
        if not isinstance(names, (tuple, list)) or len(names) != 2:
            raise ValueError("Must be a tuple or list with two strings")
        first_name, last_name = names
        self._set_name(first_name, last_name)
    
    @classmethod
    def _validate_name(cls, name):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError("Name must be alphabetic")
    
    def __str__(self):
        return self.name
    
    def _set_name(self, first_name, last_name):
        self._validate_name(first_name)
        self._validate_name(last_name)
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

actor = Person('Mark', 'Sinclair')
print(actor)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor)
# ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
character = Person('Da5id', 'Meier')
# # ValueError: Name must be alphabetic.

# friend = Person('Lynn', 'Blake')
# print(friend.name)             # Lynn Blake
# friend.name = ('Lynn', 'Blake-John')
# # ValueError: Name must be alphabetic.


    