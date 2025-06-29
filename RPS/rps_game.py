"""
Rock Paper Scissors is a two-player game 
where each player chooses one of three possible moves: rock, paper, or scissors. 
The chosen moves will then be compared to see who wins, according to the following rules:

rock beats scissors (rock crushes scissors)
scissors beats paper (scissors cut paper)
paper beats rock (paper wraps rock)
If the players choose the same move, then it's a tie.
"""
import os
import time
from rps import Computer, Human
from rules_mixin import RulesMixIN

GRAND_WINNER = "You are the GRAND WINNER! Congratulations!"
GRAND_LOSER = "The computer is the GRAND WINNER! Better luck next time!"
FINAL_SCORE = 5  # The score needed to win the game

COMPUTER_STRATEGIES = ['random', 'r2d2', 'hal', 'daneel']

class RPSGame(RulesMixIN):

    """
    Manages a single round of Rock Paper Scissors 
    between a human and the computer.

    Responsibilities:
    - Initialize players.
    - Handle user interaction (welcome, input, results).
    - Trigger player move selection.
    - Display the outcome of the match.
    """
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

        self._human_score = 0
        self._computer_score = 0

        self._saved_moves = []

    @staticmethod
    def point_to_prompt(message):
        """
        Formats a message to be displayed in the console.
        Prints ==> before the message
        """
        return '==> ' + message

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors!")

    def _display_goodbye_message(self):
        print("\nThanks for playing Rock Paper Scissors! Goodbye!")

    def _display_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'You chose: {human_move.name.upper()}')
        print(f'The computer chose: {computer_move.name.upper()}')

        if human_move == computer_move:
            print(self.point_to_prompt ("It's a tie! Well, that's lame. Try again?"))
            return 'tie'
        if human_move.beats(computer_move):
            print(self.point_to_prompt ("You WON! Congratulations!"))
            self._human_score += 1
            return 'win'
        print(self.point_to_prompt ("You are a LOSER! Better luck next time!"))
        self._computer_score += 1
        return 'lose'

    def _display_scores(self):
        """
        Displays the current scores of the human and computer players.
        """
        print("Current Scores:\n")
        print(f'You: {self._human_score} | Computer: {self._computer_score}')

    def _check_grand_winner(self):
        """
        Checks if there is a grand winner based on the scores.
        If one player has a score of 3, they are declared the grand winner.
        """
        if self._human_score >= FINAL_SCORE:
            print('+=' + '=' * len(GRAND_WINNER) + '=+')
            print(self.point_to_prompt(GRAND_WINNER))
            print('+=' + '=' * len(GRAND_WINNER) + '=+')
            print(f"You have won {FINAL_SCORE} rounds! Resetting scores...")
            self._reset_scores()
        elif self._computer_score >= FINAL_SCORE:
            print('+=' + '=' * len(GRAND_LOSER) + '=+')
            print(self.point_to_prompt (GRAND_LOSER))
            print('+=' + '=' * len(GRAND_LOSER) + '=+')
            print(f"The computer has won {FINAL_SCORE} rounds! Resetting scores...")
            self._reset_scores()

    def _reset_scores(self):
        """
        Resets the scores of both players to zero.
        """
        self._human_score = 0
        self._computer_score = 0
        print("Scores have been reset.\n")

    def play_again(self):
        """
        Asks the user if they want to play another round.

        Returns:
            bool: True if the user wants to play again (input starts with 'y'),
                  False otherwise.
        """
        ask_again = self.point_to_prompt   ("Would you like to play again? (y/n) ")
        answer = input(ask_again)
        return answer.lower().startswith('y')

    def _save_choices(self):
        self._saved_moves.append(
            (self._human.move.name, self._computer.move.name)
            )

    def return_saved_moves(self):
        """
        Prints the saved moves from the game.
        """
        for rounds, (play_choice, comp_choice) in enumerate(self._saved_moves, start=1):
            print(f'Round {rounds}:')
            print(self.point_to_prompt (f'You chose {play_choice}'))
            print(self.point_to_prompt (f'The computer chose {comp_choice}'))

    def _choose_computer_strategy(self):
        """
        Ask user to choose a computer strategy.
        If user doesn't input anything, default to 'computer'.
        Invalid choice will prompt user to choose again.
        """
        print("Choose a computer strategy:")
        print("1. Random (default)")
        print("2. R2D2")
        print("3. HAL")
        print("4. Daneel")

        choice = input("Enter your choice (1-4): ")
        if choice in {'1', '2', '3', '4'}:
            self._computer.strategy = COMPUTER_STRATEGIES[int(choice) - 1]
        else:
            print("Invalid choice, defaulting to 'Random'.")
            self._computer.strategy = 'random'

    def play(self):
        """
        Runs the main game loop for Rock Paper Scissors.

        Handles the following:
        - Welcomes the player.
        - Repeats rounds of gameplay where the human and computer choose moves.
        - Displays the outcome of each round.
        - Asks the player if they want to play again.
        - Says goodbye when the player exits.
        """
        self._display_welcome_message()
        self._display_rules()

        self._choose_computer_strategy()
        print(f'You are playing against {self._computer.strategy}')
        self._computer = Computer(self._computer.strategy)
        self._computer.set_human(self._human)

        while True:

            self._human.choose()
            self._computer.choose()
            self._computer.previous_human_move = self._human.move
            self._save_choices()


            self._display_winner()
            self._display_scores()

            self._check_grand_winner()

            if not self.play_again():
                break

            time.sleep(1)  # Pause for a moment before the next round
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        self.return_saved_moves()
        self._display_goodbye_message()
