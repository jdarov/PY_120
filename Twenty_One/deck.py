import random

class Card:
    
    FACE_VALUES = {
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        'Ace': 11,
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):
        return self._rank
    @rank.setter
    def rank(self, rank_value):
        if not hasattr(Deck, 'RANKS'):
            raise AttributeError("Deck must have a RANKS attribute defining card ranks")
        if rank_value not in getattr(Deck, "RANKS"):
            raise ValueError(f"{rank_value} is not a valid rank. Valid ranks: {Deck.RANKS}")
        self._rank = rank_value

    @property
    def suit(self):
        return self._suit
    @suit.setter
    def suit(self, card_suit):
        if not isinstance(card_suit, str):
            raise TypeError("Suit must be a valid string")
        if not hasattr(Deck, 'SUITS'):
            raise AttributeError("Deck must have a SUITS attribute defining card suits")
        if card_suit not in getattr(Deck, "SUITS"):
            raise ValueError(f"{card_suit} is not a valid rank. Valid ranks: {Deck.SUITS}")
        self._suit = card_suit

    def get_value(self):
        return self.FACE_VALUES.get(self.rank, self.rank)
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __add__(self, other):
        return (self.FACE_VALUES.get(self.rank, self.rank) +
                other.FACE_VALUES.get(other.rank, other.rank))

class Deck:

    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._deck = [Card(rank, suit) for rank in self.RANKS for suit in self.SUITS]
        self.shuffle_cards()

    def shuffle_cards(self):
        random.shuffle(self._deck)
    
    def draw(self):
        if not self._deck:
            print("Deck is empty. Reshuffling a new deck...")
            self._deck = [Card(rank, suit) for rank in self.RANKS for suit in self.SUITS]
            self.shuffle_cards()
        return self._deck.pop()