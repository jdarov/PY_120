"""
mixins.py

This module provides mixin classes for inheriting common functionality across the Tic Tac Toe game,
including screen-clearing, rule display, and user-facing messages. These are intended to be used 
in conjunction with other classes via multiple inheritance.
"""

import os
import time
from players import Human

FINAL_WINNING_ROUNDS = 5


class RulesMixIn:
    """Mixin class providing game rule display and screen clearing utilities."""

    @staticmethod
    def _clear_screen():
        """
        Clear the console screen after user input.

        Uses `cls` for Windows and `clear` for Unix-based systems.
        Includes a 1-second pause for user experience.
        """
        input("Press enter to continue...")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


    def display_rules(self):
        """
        Display the rules for Tic Tac Toe.

        Shows board layout, symbols used, gameplay instructions,
        and winning conditions for the match.
        """
        print("=" * 30)
        print("     TIC TAC TOE RULES     ")
        print("=" * 30)
        print("\nHow to Play:")
        print("- The game is played on a 3x3 grid like this:\n")

        sample_board = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        for row in sample_board:
            print(" | ".join(row))
            if row != sample_board[-1]:
                print("--+---+--")

        print("\n- Player 1 is 'X' and Player 2 is 'O'.")
        print("- Players take turns placing their symbol on an empty square.")
        print("- The first to get 3 of their symbol in a row (horizontally, vertically, "
              "or diagonally) wins the round.")
        print("- If all 9 squares are filled and no one has 3 in a row, the round is a tie.")

        print("\nHow to Win the Match:")
        print("- The game is played as a 'Best of 5' series.")
        print("- The first player to win 5 rounds is the GRAND WINNER!.")
        print("- Ties do not count toward the win count.")

        print("\nGood luck, and play smart!")
        print("=" * 30)
        self._clear_screen()

    def public_method(self):
        """
        Public method for pylint to be happy with the mixin.
        """
        return 0


class MessagesMixIn(RulesMixIn):
    """
    Mixin class that extends RulesMixIn to include user-facing messages during gameplay.
    Provides welcome, goodbye, and victory messages.
    """

    def __init__(self):
        self._human = None

    def is_winner(self, player):
        """
        Placeholder for checking if the given player is the winner.
        This method must be implemented by the inheriting class.
        """
        raise NotImplementedError("Subclasses must implement 'is_winner' method.")

    def display_welcome_message(self):
        """
        Display a welcome message before the game starts.

        Prompts the human player for their name and sets it in the Human object.
        """
        print("=" * 33)
        print("  Welcome to Tic Tac Toe! 🎮")
        print("=" * 33)
        print("Get ready for a classic showdown.")
        print("Player 1 is 'X'  |  Player 2 is 'O'")
        print(f"First to win {FINAL_WINNING_ROUNDS} rounds takes the match!")
        print("Let the best player win. Good luck!\n")
        print("Before we start, let's pick a name for the player.\n")
        self._human = Human(
            input("<Please enter a name for the player: > ").capitalize()
        )

    def display_goodbye_message(self):
        """
        Display a goodbye message after the game concludes.

        Shows different messages based on whether the human player won or lost.
        """
        print("*" * 40)
        print(f"Thanks for playing, {self._human.name}!\n")

        if self.is_winner(self._human):
            print(f"{self._human.name} is the Tic Tac Toe Champion! 🥇")
            print("Victory is yours. Well played, legend! 🎉")
        else:
            print("You fought bravely, but the grid was cruel. 😅")
            print("Better luck next time. Keep training, warrior! 💪")

        print("Goodbye for now! Come back anytime.\n")
        print("*" * 40)

    def display_grand_winner(self, winner):
        """
        Display a celebratory message for the grand winner of the match.

        Args:
            winner (Player): The player object who won the match.
        """
        banner_text = (f"CONGRATULATIONS!!!!! <{winner.name.upper()}>! \n"
                       f"You are the GRAND WINNER! 🏆")
        banner_border = "+=" + "=" * len(banner_text) + "=+"

        print(banner_border)
        print(banner_text)
        print("You have proven your skill and strategy on the Tic Tac Toe battlefield.")
        print("Your name will be remembered in the annals of Tic Tac Toe history! 🎖️")
        print(banner_border)
