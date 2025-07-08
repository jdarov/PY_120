from highest_lowest_cards import Card
import random

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.reset_deck()

    def reset_deck(self):
        self._deck = [Card(rank, suit) for rank in self.RANKS for suit in self.SUITS]
        random.shuffle(self._deck)

    def draw(self):
        if not self._deck:
            self.reset_deck()
        return self._deck.pop()
