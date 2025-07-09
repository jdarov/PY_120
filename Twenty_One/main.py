import os
import time
from twenty_one import TwentyOne
from rules_mix_in import RulesMixin

class Main(RulesMixin):
    
    CONTINUE = {'yes', 'y'}
    DONT_CONTINUE = {'no', 'n'}
    VALID_RESPONSES = CONTINUE | DONT_CONTINUE

    GRAND_SCORE = 5

    ROUNDS = 1

    PROMPT = 'Do you want to play again? (y/n) '
    ASK_NAME = "Who is playing today? \n==>Please enter your name: "
    
    
    def __init__(self):
        self._game = None
        self._continue = True

        self._player_score = self._dealer_score = 0
        self._player_name = input(self.ASK_NAME).capitalize()

        self.WIN_MSG = (f"CONGRATULATIONS! {self._player_name}"
                          f' is the GRAND WINNER! Luck was on your side today!')
        self.LOSE_MSG = (f'DEALER is the GRAND WINNER....'
                         f'{self._player_name}, you should learn to count cards!')
        
   
    @staticmethod
    def _clear_screen():
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def continue_game(self):
        while True:
            user_choice = input(self.PROMPT).strip().lower()
            if user_choice in self.VALID_RESPONSES:
                if user_choice in self.CONTINUE:
                    self.ROUNDS += 1
                    self._continue = True
                    self._clear_screen()
                    return
                self._continue = False
                return
            print("Invalid input.")

    def show_scores(self):
        print()
        print(f'Scoreboard: Player {self._player_score} | '
              f'Dealer {self._dealer_score}')
        print('-'*50)
    
    def grand_winner(self):
        if self._player_score == self.GRAND_SCORE:
            print(f'+=' + f'='*len(self.WIN_MSG) + f'=+')
            print(f'| ' + f'{self.WIN_MSG}' + f' |')
            print(f'+=' + f'='*len(self.WIN_MSG) + f'=+')
            self._player_score = self._dealer_score = 0
            return
        print(f'+=' + f'='*len(self.LOSE_MSG) + f'=+')
        print(f'| ' + f'{self.LOSE_MSG}' + f' |')
        print(f'+=' + f'='*len(self.LOSE_MSG) + f'=+')
        self._player_score = self._dealer_score = 0
        return
    
    def main(self):
        self.display_rules()
        print(f"Welcome to Twenty One {self._player_name}!")
        print('='*50)
        while self._continue:
            print(f'-'*10 + f'ROUND {self.ROUNDS}' + '-'*10)
            self._game = TwentyOne(self._player_name)
            winner = self._game.play()

            #update scores manually
            if winner == 'player':
                self._player_score += 1
            elif winner == 'dealer':
                self._dealer_score += 1
            
            self.show_scores()
            if self.GRAND_SCORE in (self._player_score, self._dealer_score):
                self.grand_winner()
            self.continue_game()



if __name__ == '__main__':
    play_twenty_one = Main()
    play_twenty_one.main()