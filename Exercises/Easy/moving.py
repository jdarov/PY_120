class WalkMixIn:

    def walk(self):
        if hasattr(self, 'title'):
            return f'{self.title} {self.name} {self.gait()} forward'
        return f'{self.name} {self.gait()} forward'

class Person(WalkMixIn):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(WalkMixIn):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixIn):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"

class Noble(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self._title = title
    @property
    def title(self):
        return self._title
    def gait(self):
        return 'struts'


mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"