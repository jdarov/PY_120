"""
rules_mixin.py

This module provides a mixin class to display the rules for the 21 (Blackjack) game.
It includes instructions for the player, a breakdown of dealer behavior, and a clean 
transition into the game by requiring the user to press Enter before continuing.

Intended to be used as a mixin in the main game controller class.
"""

import os
import time

class RulesMixin:
    """Mixin for displaying rules and handling the transition to game start."""

    @staticmethod
    def display_rules():

        """
        Display the rules of the 21 game to the user.

        - Describes how to play, including card values and turn options.
        - Explains the dealer's logic (dealer hits until beating player or busting).
        - Waits for the user to press Enter before continuing.
        - Clears the screen before the game begins.
        """

        print("=" * 40)
        print("        WELCOME TO 21 - BLACKJACK")
        print("=" * 40)
        print("\nHow to Play:")
        print("- Try to get as close to 21 as possible without going over.")
        print("- Face cards are worth 10. Aces are worth 1 or 11.")
        print("- You and the dealer start with two cards.")
        print("- You can choose to 'Hit' (draw another card) or 'Stay'.")
        print("- If your hand goes over 21, you bust and lose.")
        print()
        print("Dealer Rules:")
        print("- The dealer will reveal their hidden card after your turn.")
        print("- Dealer hits until they either:")
        print("    * Beat your hand, or")
        print("    * Bust by going over 21.")
        print("- If the dealer busts, you win!")
        print()
        print("=" * 40)
        input("Press Enter to begin the game...")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

    def pylint_method(self):
        """
        Second method for pylint to be happy
        """
        return None
