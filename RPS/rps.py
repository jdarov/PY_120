"""
RPS Game Logic Module

This module contains the core logic and structure for a 
Rock Paper Scissors game,
including support classes for:

players, moves, and rule evaluation.

Features:
- Human and computer players.
- Input validation with support for shorthand and ambiguous input resolution.
- Placeholder classes for Move and Rule, 
    allowing easy expansion (e.g., RPSLS variant).
"""


import random

class Player:
    """
    Represents a player in the Rock Paper Scissors game.

    Attributes:
    - player_type (str): 'human' or 'computer'
    - move (str): The selected move for the round

    Methods:
    - choose(): Prompts human input or randomly selects computer move
    - _get_valid_player_choice(): Validates and parses human input
    - _return_long_from_short(): Resolves shorthand input into full move names
    """

    SHORT_CHOICES = {'s', 'sp', 'sc', 'r', 'p', 'l'}
    VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    def __init__(self):
        self.move = None
        self._choice = None
        self._full_choice = None

    def return_long_from_short(self, play_choice):
        """
        Resolves shorthand user input into a full move name.

        Specifically handles ambiguous shorthand like 's' by prompting
        for clarification between 'scissors' and 'spock'. Returns the
        fully qualified move string in lowercase.

        Args:
            play_choice (str): The user's input, possibly shorthand.

        Returns:
            str: The resolved full move name (e.g., 'rock', 'spock').
        """
        if play_choice in Player.SHORT_CHOICES:
            while play_choice == 's':
                play_choice = input('Did you mean spock(sp) or scissors(sc)? ')
                if play_choice not in {'spock', 'scissors', 'sp', 'sc'}:
                    print("That wasn't a valid clarification")
                    play_choice = 's'
            for choice in Player.VALID_CHOICES:
                if choice.startswith(play_choice):
                    return choice.lower()
        return play_choice.lower()

    def get_valid_player_choice(self):
        """
        Continuously prompts the user for a valid move choice.

        Handles input validation, resolves shorthand using
        `return_long_from_short()`, and ensures the final result is one of
        the accepted valid choices (including RPSLS options).

        Returns:
            str: A validated move chosen by the player.
        """
        while True:
            print(f"Choose one: {', '.join(Player.VALID_CHOICES)}")
            self._choice = input().strip().lower()
            self._full_choice = self.return_long_from_short(self._choice)
            if self._full_choice in Player.VALID_CHOICES:
                return Move.move_class(self._full_choice)
            print("That is not a valid choice! Please try again.")

class Computer(Player):
    """
    Represents a computer-controlled player in the Rock Paper Scissors game.

    Inherits from the Player class and overrides the choose() method to 
    automatically select a move at random from the available choices 
    (rock, paper, scissors).

    Attributes:
    - move (str): The randomly selected move for the round.

    Methods:
    - choose(): Randomly selects and sets a move from Player.CHOICES.
    """

    def __init__(self, computer_name='random'):
        super().__init__()
        self._computer_name = computer_name
        self._first_turn = True
        self._human = None

        self.previous_human_move = None

        self._strategy = {
            'random': self.choose_random,
            'r2d2': self.choose_r2d2,
            'hal': self.choose_hal,
            'daneel': self.choose_daneel
        }
        if self._computer_name not in self._strategy:
            raise ValueError(f"Unknown computer type: {self._computer_name}. "
                             "Valid types are: 'random', 'r2d2', 'HAL', 'Daneel'.")

        self._choose = self._strategy[self._computer_name]

    def set_human(self, human_player):
        """
        Sets the human player for the computer to reference.
        """
        self._human = human_player

    def choose_random(self):
        """
        Chooses a computer move at random from a list of 
        valid choices (rock, paper, scissors, lizard, spock)
        """
        choice = random.choice(Player.VALID_CHOICES)
        self.move = Move.move_class(choice)

    def choose_r2d2(self):
        """
        R2D2's strategy: always chooses 'rock'.
        """
        self.move = Move.move_class('rock')

    def choose_hal(self):
        """
        HAL's strategy: choose scissors about 2/3 of the time
        Pick random choice 1/3 of the time
        """
        if random.random() < 0.6667:
            self.move = Move.move_class('scissors')
        else:
            other_choices = [choice for choice in Player.VALID_CHOICES if choice != 'scissors']
            choice = random.choice(other_choices)
            self.move = Move.move_class(choice)
    def choose_daneel(self):
        """
        Daneel's strategy: always choose the Human players last move
        First move is always a random move
        """
        if self._first_turn:
            # If no human player is set or no move has been made yet,
            # choose a random move.
            self.choose_random()
            self._first_turn = False
        else:
            # If a human player is set and has made a move, use that move.
            self.move = Move.move_class(self.previous_human_move.name)
    def choose(self):
        """
        Overrides the choose method from Player class.
        Randomly selects a move based on the computer's strategy.
        """
        return self._choose()

class Human(Player):
    """
    Represents a human player in the Rock Paper Scissors game.

    Inherits from the Player class and prompts the user for input
    to choose a move. Supports both full and shorthand input with
    clarification for ambiguous entries like 's'.

    Methods:
    - choose(): Interactively prompts the user to select a valid move.
    """
    def choose(self):
        """
        Overrides any other choose methods
        Prompts the user for a valid choice from list of choices
        Exceps shorthand responses (s, sp, sc, r, p, l)
            and converts to full choice equivalent
        """
        self.move = self.get_valid_player_choice()

class Move:
    """
    Abstract base class for moves in the Rock Paper Scissors game.
    """
    name = ""

    def __eq__(self, other):
        return (isinstance(other, Move) and
                self.name == other.name)

    def __str__(self):
        return self.name

    def beats(self, other):
        """
        Determines if this move beats another move.
        
        This method should be overridden in subclasses to define
        the specific rules of which moves beat which.
        
        Args:
            other (Move): The move to compare against.
        
        Returns:
            bool: True if this move beats the other move, False otherwise.
        """
        return other.name in self.WINS_AGAINST.get(self.name, [])

    @staticmethod
    def move_class(move_name):
        """
        Factory method to create a move instance based on the move name.
        
        Args:
            move_name (str): The name of the move (e.g., 'rock', 'paper').
        
        Returns:
            Move: An instance of the corresponding move class.
        """
        move_classes = {
            'rock': Rock,
            'paper': Paper,
            'scissors': Scissors,
            'lizard': Lizard,
            'spock': Spock
        }
        try:
            return move_classes[move_name.lower()]()
        except KeyError as exc:
            raise ValueError(f"Invalid move name: {move_name}. "
                             "Valid moves are: " 
                             "rock, paper, scissors, lizard, spock.") from exc
    WINS_AGAINST = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard' : ['spock', 'paper'],
        'spock' : ['scissors', 'rock']
    }

class Rock(Move):
    """
    Represents the 'Rock' move in the game.

    Inherits from the base Move class.
    Rock beats Scissors and Lizard.
    """
    name = "rock"

class Paper(Move):
    """
    Represents the 'Paper' move in the game.

    Inherits from the base Move class.
    Paper beats Rock and Spock.
    """
    name = "paper"

class Scissors(Move):
    """
    Represents the 'Scissors' move in the game.

    Inherits from the base Move class.
    Scissors beats Paper and Lizard.
    """
    name = "scissors"

class Lizard(Move):
    """
    Represents the 'Lizard' move in the game.

    Inherits from the base Move class.
    Lizard beats Spock and Paper.
    """
    name = "lizard"

class Spock(Move):
    """
    Represents the 'Spock' move in the game.

    Inherits from the base Move class.
    Spock beats Scissors and Rock.
    """
    name = "spock"
