import random
import math

class GuessingGame():

    def __init__(self, low, high):
        self._total_number_of_guesses = int(math.log2(high - low + 1)) + 1
        self._low = low
        self._high = high 

    def _number_of_guesses(self):
        print(f'You have {self._total_number_of_guesses} guesses remaining.')
        self._total_number_of_guesses -= 1

    def _enter_a_number(self):
        prompt = f"Enter a number between {self._low} and {self._high}: "
        while True:
            try:
                guess = int(input(prompt))
            except ValueError:
                print("You must enter a valid number")
                continue
            if not self._low <= guess <= self._high:
                prompt = f"Invalid number: Enter a number between {self._low} and {self._high}: "
                continue
            return guess
        
    def _validate_guess(self, guess):
        if guess < self._random_number:
            print("Your guess is too low.")
            return False
        if guess > self._random_number:
            print('Your guess is too high.')
            return False
        print("That's the number!")
        return True

    def play(self):
        self._random_number = random.randint(self._low, self._high)

        while self._total_number_of_guesses:

            self._number_of_guesses()
            guess = self._enter_a_number()

            if self._validate_guess(guess):
                print("\nYou won!")
                return
            
        print("\nYou have no more guesses. You lost!")

game = GuessingGame(501, 1500)

game.play()