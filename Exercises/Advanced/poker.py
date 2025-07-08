from collections import Counter
from Deck_Of_Cards import Deck
from highest_lowest_cards import Card


class PokerHand:
    def __init__(self, deck):
        self._deck = deck
        self._hand = [self._deck.draw() for _ in range(5)]
        self._hand_ranks = [Card.FACE_VALUES[card.rank] for card in self._hand]
        self._hand_suits = [card.suit for card in self._hand]

    def display_hand(self):
       for card in self._hand:
           print(card)
           

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():

            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        royal = {14, 10, 11, 12, 13}
        return self._is_flush() and set(self._hand_ranks) == royal
        
    def _is_straight_flush(self):
        return self._is_straight() and self._is_flush()

    def _is_four_of_a_kind(self):
        return any(self._hand_ranks.count(rank) == 4 for rank in self._hand_ranks)

    def _is_full_house(self):
        return self._is_pair() and self._is_three_of_a_kind()

    def _is_flush(self):
        return len(set(self._hand_suits)) == 1

    def _is_straight(self):
        sorted_ranks = sorted(self._hand_ranks)
        return (all(b == a+1 for a, b in zip(sorted_ranks, sorted_ranks[1:])) or
                sum(sorted_ranks[:-1]) == sorted_ranks[-1])

    def _is_three_of_a_kind(self):
        return any(self._hand_ranks.count(rank) == 3 for rank in self._hand_ranks)

    def _is_two_pair(self):
        counts = Counter(self._hand_ranks).values()
        return list(counts).count(2) == 2
    
    def _is_pair(self):
        return (any(self._hand_ranks.count(rank) == 2 for rank in self._hand_ranks)
                and not self._is_two_pair())

hand = PokerHand(Deck())
hand.display_hand()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card(3, "Hearts"),
            Card(4, "Hearts"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")
