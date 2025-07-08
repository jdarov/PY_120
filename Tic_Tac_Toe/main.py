"""
Main entry point for running the Tic Tac Toe game.

This module initializes the game, prompts the user to choose who plays first,
and manages the main gameplay loop.
"""

from tic_tac_toe import TTTGame as game

class Main:
    """
    Controls the flow of the Tic Tac Toe game, including player selection
    and game loop management.
    """

    def __init__(self):
        """
        Initialize the game and prompt the user to select who goes first.
        """
        self._game = game()
        self.first_player = ''
        self._game.display_rules()
        while not self.first_player:
            self.first_player = input(
                "Who plays first? (1 for Human, 2 for Computer): "
            )
            if self.first_player not in ['1', '2']:
                print("Invalid choice. Please enter '1' for Human or '2' for Computer.")
                self.first_player = ''

    def play(self):
        """
        Start and manage the main game loop, including game resets and end conditions.
        """
        self._game.clear_screen()
        self._game.display_welcome_message()
        self._game.clear_screen()

        while True:
            if self._game.is_game_over():
                if not self._game.display_results():
                    break
                if not self._game.play_again():
                    break
                self._game.clear_screen()
                self._game.reset_board()
            if self.first_player == '1':
                self._game.human_play()
            else:
                self._game.computer_play()

        self._game.display_goodbye_message()
    def second_method(self):
        """
        Placeholder for a second method if needed in the future.
        """
        return 0


main = Main()

if __name__ == "__main__":
    main.play()
