"""
players.py

This module defines the player classes for the Tic Tac Toe game,
including a base Player class, a Human player class, and a Computer
player with basic AI for offensive and defensive strategy.
"""

import random
import codecs
from board import Square


class Player:
    """
    Base class representing a player in the game.
    """

    DEFAULT_SCORE = 0

    def __init__(self, marker):
        """
        Initialize a player with a marker and default score.
        """
        self._marker = marker
        self._score = self.DEFAULT_SCORE

    @property
    def marker(self):
        """Return the player's marker (e.g., 'X' or 'O')."""
        return self._marker

    @marker.setter
    def marker(self, value):
        """Set the player's marker."""
        self._marker = value

    @property
    def score(self):
        """Return the player's current score."""
        return self._score

    @score.setter
    def score(self, new_score):
        """
        Set the player's score to a non-negative integer.
        """
        if isinstance(new_score, int) and new_score >= 0:
            self._score = new_score
        else:
            raise ValueError("Score must be a non-negative integer.")

    def __iadd__(self, other):
        """
        Increment player's score using += operator.
        """
        if isinstance(other, int) and other >= 0:
            self._score += other
            return self
        raise ValueError("Can only add a non-negative integer to score.")


class Human(Player):
    """
    Represents a human player in the game.
    """

    def __init__(self, player_name=None):
        super().__init__(Square.HUMAN_MARKER)
        self.name = player_name

    @property
    def name(self):
        """Return the player's name."""
        return self._name

    @name.setter
    def name(self, player_name):
        """
        Validates and sets the player's name.
        Falls back to 'Player' if input is invalid or empty.
        """
        if isinstance(player_name, str):
            try:
                player_name = codecs.decode(player_name, 'unicode_escape')
            except UnicodeDecodeError:
                pass
            cleaned_name = player_name.strip()
        else:
            cleaned_name = ''

        if not cleaned_name:
            print("Name must be a non-empty string.")
            print("Setting name to default 'Player'")
            cleaned_name = 'Player'

        self._name = cleaned_name

    def mark(self, board, position):
        """
        Marks a square on the board if the move is valid.
        """
        if board.is_valid_move(position):
            board.place_marker(self.marker, position)
        else:
            raise ValueError("Invalid move")


class Computer(Player):
    """
    Represents the computer player with basic AI logic.
    """

    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)
        self.name = "Computer"

    def mark(self, board, position):
        """
        Marks a square on the board if the move is valid.
        """
        if board.is_valid_move(position):
            board.place_marker(self.marker, position)
        else:
            raise ValueError("Invalid move")

    def _defense(self, board):
        """
        Looks for a row where the human has 2 markers
        and blocks the third square.
        """
        for row in board.POSSIBLE_WINNING_ROWS:
            if board.count_markers_for(Square.HUMAN_MARKER, row) == 2:
                for pos in row:
                    if board.squares[pos].is_unused():
                        return pos
        return None

    def _offense(self, board):
        """
        Looks for a row where the computer has 2 markers
        and completes the win.
        """
        for row in board.POSSIBLE_WINNING_ROWS:
            if board.count_markers_for(Square.COMPUTER_MARKER, row) == 2:
                for pos in row:
                    if board.squares[pos].is_unused():
                        return pos
        return None

    def _middle(self, board):
        """
        Checks if the center square is available.
        """
        return board.squares[5].is_unused()

    def move(self, board):
        """
        Determines and makes the best move for the computer:
        1. Try to win.
        2. Block opponent's winning move.
        3. Take the center square.
        4. Pick a random square.
        """
        winning_move = self._offense(board)
        if winning_move:
            board.mark_square(winning_move, self.marker)
            return

        blocking_move = self._defense(board)
        if blocking_move:
            board.mark_square(blocking_move, self.marker)
            return

        if self._middle(board):
            board.mark_square(5, self.marker)
            return

        available_squares = board.unused_squares()
        if available_squares:
            random_move = random.choice(available_squares)
            board.mark_square(random_move, self.marker)
            return
