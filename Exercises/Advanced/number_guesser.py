import random

class GuessingGame():

    def __init__(self):
        self._total_number_of_guesses = 7

    def _number_of_guesses(self):
        print(f'You have {self._total_number_of_guesses} guesses remaining.')
        self._total_number_of_guesses -= 1

    @staticmethod
    def _enter_a_number():
        prompt = "Enter a number between 1 and 100: "
        while True:
            try:
                guess = int(input(prompt))
            except ValueError:
                print("You must enter a valid number")
                continue
            if not 0 <= guess <= 100:
                prompt = "Invalid number: Enter a number between 1 and 100: "
                continue
            return guess
        
    def _validate_guess(self):
        if self._user_choice < self._random_number:
            print("Your guess is too low.")
            return False
        if self._user_choice > self._random_number:
            print('Your guess is too high.')
            return False
        print("That's the number!")
        return True

    def play(self):
        self._random_number = random.randint(1, 100)

        while self._total_number_of_guesses:

            self._number_of_guesses()
            self._user_choice = self._enter_a_number()

            if self._validate_guess():
                print("\nYou won!")
                return
            
        print("\nYou have no more guesses. You lost!")

game = GuessingGame()

game.play()







            
            


    
