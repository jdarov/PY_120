import random

class ArmorMixIn:

    def attach_armor(self):
        pass
    
    def remove_armor(self):
        pass

class SpellMixIn:

    def cast_spell(self, spell):
        pass

class Player:

    def __init__(self, name='John'):
        self._name = name
        self._health = 100
        self._strength = self._roll_dice()
        self._intelligence = self._roll_dice()
    
    def _roll_dice(self):
        return random.randint(2, 12)

    @property
    def strength(self):
        return self._strength
    @property
    def intelligence(self):
        return self._intelligence
    
    @strength.setter
    def strength(self, new_strength):
        raise AttributeError("You can not change the strength once player has been created")
    @intelligence.setter
    def intelligence(self, new_intelligence):
        raise AttributeError("You can not change intelligence once player has been created")
    
    def heal(self, heal_value):
        self._health += heal_value

    def hurt(self, hurt_value):
        self._health -= hurt_value

    def __str__(self):
        return (
            f'Name: {self._name}\n'
            f'Class: {self.__class__.__name__}\n'
            f'Health: {self._health}\n'
            f'Strength: {self.strength}\n'
            f'Intelligence: {self.intelligence}'
        )

class Warrior(ArmorMixIn, Player):

    def __init__(self, name='John'):
        super().__init__(name)
        self._strength += 2

class Magician(SpellMixIn, Player):
    
    def __init__(self, name='John'):
        super().__init__(name)
        self._intelligence += 2

class Paladin(ArmorMixIn, SpellMixIn, Player):
    
    def __init__(self, name='John'):
        super().__init__(name)

class Bard(Magician):
    def create_potion(self):
        pass
