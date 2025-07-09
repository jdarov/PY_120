from deck import Deck, Card

class Participant:

    HIGHEST_TOTAL = 21
    
    def __init__(self, deck, player_name='dealer'):
        if not isinstance(deck, Deck):
            raise ValueError("You must use a valid Deck of Cards")
        self._deck = deck
        self._hand = [self._deck.draw() for _ in range(2)]
        self._stay = False

        self.name = player_name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    def stay(self):
        self._stay = True
        return self
    
    def hit(self):
        self._hand.append(self._deck.draw())
        return self

    def is_busted(self):
        return self._hand_total() > self.HIGHEST_TOTAL

    def _hand_total(self):
        total = sum(card.get_value() for card in self._hand)
        if total > self.HIGHEST_TOTAL:
            if "Ace" in (card.rank for card in self._hand):
                total -= 10 * [card.rank for card in self._hand].count('Ace')
        return total
    
    def __str__(self):
        return (f'({', '.join(f'{{{card}}}' for card in self._hand)}) '
                f'Total: {self._hand_total()}')
    
    def __gt__(self, other):
        return self._hand_total() > other._hand_total()
    def __ge__(self, other):
        return self._hand_total() >= other._hand_total()
    
    def __lt__(self, other):
        return self._hand_total() < other._hand_total()
    def __le__(self, other):
        return self._hand_total <= other._hand_total()
    
    def __eq__(self, other):
        return self._hand_total() == other._hand_total()
