class Person:

    def __init__(self, name):
        self._first_name = name
        self._last_name = ''
    @property
    def name(self):
        if self._last_name:
            return f'{self._first_name} {self._last_name}'
        return self._first_name
    @name.setter
    def name(self, new_name):
        new_names = new_name.split()
        if len(new_names) > 1:
            self._first_name = new_names[0]
            self._last_name = new_names[1]
        else:
            self._first_name = new_name
            self._last_name = ''
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, new_last_name):
        self._last_name = new_last_name
    
    def __eq__(self, other):
        return self.first_name == other.first_name
    


    
bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams

bob = Person('Robert Smith')
rob = Person('Robert Smith')

print(bob == rob) #True