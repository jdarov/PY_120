class Pet:
    def __init__(self, species, name):
        self._species = species
        self._name = name

    @property
    def name(self):
        return self._name
    @property
    def species(self):
        return self._species

    def __str__(self):
        return f'a {self.species} named {self.name}'

class Owner:
    def __init__(self, name):
        self._name = name
        self._pets = list()
    
    @property
    def name(self):
        return self._name
    @property
    def pets(self):
        return self._pets.copy()

    def add_pet(self, pet):
        self._pets.append(pet)
    
    def number_of_pets(self):
        return len(self._pets)
    
    def __str__(self):
        return f'{self.name} has adopted the following pets:'
            
    
class Shelter():
    def __init__(self):
        self._owners = list()

    def adopt(self, owner, pet):
        if owner not in self._owners:
            self._owners.append(owner)
        owner.add_pet(pet)
    
    def print_adoptions(self):
        for owner in self._owners:
            print(owner)
            for pet in owner.pets:
                print(pet)
            print('\n')






cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")


# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.