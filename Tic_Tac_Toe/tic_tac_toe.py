"""
Main game engine for Tic Tac Toe.

This module contains the TTTGame class that manages the game flow,
score tracking, player turns, win conditions, and interaction logic
between the human player and the computer opponent.
"""
import os
from board import Square, Board
from players import Computer
from messages_mixin import MessagesMixIn

POSSIBLE_WINNING_ROWS = (
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (1, 4, 7), (2, 5, 8), (3, 6, 9),
    (1, 5, 9), (3, 5, 7)
)

CONTINUE = {"yes", "y"}
TERMINATE = {"no", "n"}
VALID = CONTINUE.union(TERMINATE)

FINAL_SCORE = 3


class TTTGame(MessagesMixIn):
    """
    Tic Tac Toe game engine. Controls game flow, user input, and scoring.
    """

    def __init__(self):
        """
        Initialize the game with a board and two players.
        """
        super().__init__()
        self._board = Board()
        self._computer = Computer()

    def _join_or(self, numbers, delim=', ', final_delim='or'):
        """
        Return a human-readable string with commas and 'or' for choices.
        """
        if len(numbers) == 1:
            return str(numbers[0])
        return (
            delim.join(map(str, numbers[:-1])) +
            f' {final_delim} {numbers[-1]}'
            if len(numbers) > 2
            else f'{numbers[0]} {final_delim} {numbers[1]}'
        )

    def display_scores(self):
        """
        Display the current scores of the human and computer players.
        """
        print("=" * 40)
        print(f"Scores: You: {self._human.score} | Computer: {self._computer.score}")
        print("=" * 40)

    def human_moves(self):
        """
        Prompt the human player to make a valid move on the board.
        """
        valid_choices = self._board.unused_squares()
        while True:
            try:
                print(f'({self._join_or(valid_choices)}): \n')
                choice = int(input("==> Choose a square: "))
                if choice in valid_choices:
                    break
            except ValueError as e:
                print(e, "You must enter a number.", sep='\n')
                continue
            print(f"Invalid choice. Please choose a number {valid_choices}")
        self._board.mark_square(choice, Square.HUMAN_MARKER)

    def is_game_over(self):
        """
        Return True if the board is full or a player has won.
        """
        return self.board_is_full() or self.someone_won()

    def board_is_full(self):
        """
        Return True if there are no more unused squares.
        """
        return not self._board.unused_squares()

    def three_in_a_row(self, player, row):
        """
        Return True if the player has all markers in the given row.
        """
        return self._board.count_markers_for(player, row) == 3

    def someone_won(self):
        """
        Return True if either the human or computer has won.
        """
        return self.is_winner(self._human) or self.is_winner(self._computer)

    def is_winner(self, player):
        """
        Check if the player has any winning row.
        """
        return any(
            self.three_in_a_row(player, row) for row in POSSIBLE_WINNING_ROWS
        )

    def display_results(self):
        """
        Display the result of the current game round and update scores.
        """
        if self.is_winner(self._human):
            self.clear_screen()
            print("Congratulations! You win! 🎉")
            self._human += 1
            self._board.display()
            self.display_scores()
            if self._human.score >= FINAL_SCORE:
                self.display_grand_winner(self._human)
                return False
            return True

        if self.is_winner(self._computer):
            self.clear_screen()
            print("The computer wins this time! 🤖")
            self._computer += 1
            self._board.display()
            self.display_scores()
            if self._computer.score >= FINAL_SCORE:
                self.display_grand_winner(self._computer)
                return False
            return True

        print("It's a tie! No one wins this round. 🤝")
        self.clear_screen()
        self._board.display()
        self.display_scores()
        return True

    def clear_screen(self):
        """
        Clear the terminal screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def play_again(self):
        """
        Ask the user if they want to play another game.
        """
        while True:
            choice = input("Do you want to play again? (y/n): ").strip().lower()
            if choice in VALID:
                return choice in CONTINUE
            print("Invalid choice. Please enter 'y' or 'n'.")

    def reset_board(self):
        """
        Reset the game board for a new game.
        """
        self._board.clear_board()

    def human_play(self):
        """
        Game loop where the human player goes first.
        """
        self._board.display()
        self.display_scores()
        while True:
            self.human_moves()
            if self.is_game_over():
                break
            self._computer.move(self._board)
            self.clear_screen()
            self._board.display()
            self.display_scores()
            if self.is_game_over():
                break

    def computer_play(self):
        """
        Game loop where the computer goes first.
        """
        while True:
            self._computer.move(self._board)
            self.clear_screen()
            self._board.display()
            self.display_scores()
            if self.is_game_over():
                break
            self.human_moves()
            if self.is_game_over():
                break
