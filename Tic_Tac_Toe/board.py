
"""
Tic Tac Toe Board and Square classes.

This module defines the structure of the game board and the individual squares
used in a Tic Tac Toe game. It includes functionality to mark, check, and display
the board's state as well as identify potential winning rows.
"""

class Square:
    """
    Represents a single square on the Tic Tac Toe board.

    Attributes:
        INITIAL_MARKER (str): Default marker for an unused square.
        HUMAN_MARKER (str): Marker representing the human player.
        COMPUTER_MARKER (str): Marker representing the computer player.
    """

    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        """
        Initialize a Square with an optional marker.

        Args:
            marker (str): The marker for the square. Defaults to INITIAL_MARKER.
        """
        self._marker = marker

    @property
    def marker(self):
        """
        Get the current marker of the square.

        Returns:
            str: The marker.
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """
        Set the marker for the square.

        Args:
            marker (str): The marker to be set.
        """
        self._marker = marker

    def __str__(self):
        """
        String representation of the square.

        Returns:
            str: The marker as string.
        """
        return self._marker

    def is_unused(self):
        """
        Check if the square is unused.

        Returns:
            bool: True if square is unused, False otherwise.
        """
        return self._marker == self.INITIAL_MARKER


class Board:
    """
    Represents the Tic Tac Toe game board.

    Attributes:
        POSSIBLE_WINNING_ROWS (tuple): All possible winning row combinations.
    """

    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
        (1, 5, 9), (3, 5, 7)              # Diagonal
    )

    def __init__(self):
        """
        Initialize the board with 9 squares.
        """
        self.squares = {pos: Square() for pos in range(1, 10)}

    def is_unused_square(self, position):
        """
        Check if a given square is unused.

        Args:
            position (int): The position on the board (1-9).

        Returns:
            bool: True if unused, False otherwise.
        """
        return self.squares[position].is_unused()

    def unused_squares(self):
        """
        Get a list of all unused square positions.

        Returns:
            list: Positions (int) of unused squares.
        """
        return [pos for pos, square in self.squares.items() if square.is_unused()]

    def mark_square(self, position, marker):
        """
        Mark a square with a given marker.

        Args:
            position (int): The position to mark.
            marker (str): The marker to use ('X' or 'O').
        """
        self.squares[position].marker = marker

    def count_markers_for(self, player, keys):
        """
        Count how many squares in a row contain the player's marker.

        Args:
            player (str or object): The player or marker to check.
            keys (iterable): List of board positions to check.

        Returns:
            int: Number of matching markers.
        """
        marker = player if isinstance(player, str) else player.marker
        return sum(1 for key in keys if self.squares[key].marker == marker)

    def clear_board(self):
        """
        Reset all squares on the board to their initial state.
        """
        for square in self.squares.values():
            square.marker = Square.INITIAL_MARKER

    def display(self):
        """
        Print a visual representation of the board to the console.
        """
        print()
        print("     |     |     ")
        print(f"  {self.squares[1]}  |  {self.squares[2]}  |  {self.squares[3]}  ")
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        print(f"  {self.squares[4]}  |  {self.squares[5]}  |  {self.squares[6]}  ")
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        print(f"  {self.squares[7]}  |  {self.squares[8]}  |  {self.squares[9]}  ")
        print("     |     |     ")
        print()
