from participants import Participant
from deck import Deck


class TwentyOne:

    VALID_MOVES = {'hit', 'stay', 'h', 's'}

    WINNNING_SCORE = 21

    def __init__(self, player_name):
        self._new_deck = Deck()

        self._player = Participant(self._new_deck, player_name)
        self._dealer = Participant(self._new_deck)

        self._player_score = 0
        self._dealer_score = 0

    
    @staticmethod
    def _point_to_prompt(prompt):
        return f'==> {prompt}'
    
    def _determine_winner(self):

        if self._player.is_busted():
            print(f'{self._player.name} BUSTED! Dealer wins :(')
            return 'dealer'
        if self._dealer.is_busted():
            print("Dealer BUSTED! HAHA what a loser :)")
            return 'player'
        
        if self._player > self._dealer:
            print(f'{self._player.name} wins! Keep going baby!')
            return 'player'
        if self._player < self._dealer:
            print('Dealer wins....')
            return 'dealer'
        
        print("That's a push(tie).")
        return ''
    
    def show_results(self):
        print("="*60)
        print(f'Dealer has: {self._dealer}')
        print(f'{self._player.name} has: {self._player}')
        print("="*60)

    def _validate_decision(self, prompt):
        while True:
            user_decision = input(prompt).strip().lower()
            if user_decision in self.VALID_MOVES:
                return 'hit' if user_decision in {'hit', 'h'} else 'stay'
            print("That was not a valid input.")

    def play(self):

        print(f'Dealer has ({{{self._dealer._hand[0]}}} and ?)>, '
                f'Total: {self._dealer._hand[0].get_value()}')
        print(f'{self._player.name} has {self._player}')
        
        print(self._point_to_prompt('Your turn...'))

        while not self._player._stay:
            self._decision = self._validate_decision("Hit or Stay? (h/s): ")
            getattr(self._player, self._decision)()
            print(f'{self._player.name} has {self._player}')
            if self._player.is_busted():
                print(self._point_to_prompt("You BUSTED!"))
                break
        
        if not self._player.is_busted():
            print(f'{self._player.name} stays at {self._player._hand_total()}')
            print(self._point_to_prompt("Dealer's Turn...."))

            while not self._dealer._stay:
                print(f'Dealer has {self._dealer}')
                if self._dealer.is_busted():
                    print(self._point_to_prompt("Dealer BUSTED!"))
                    break
                if (self._dealer < self._player and
                    self._dealer._hand_total() < 17):
                    print(self._point_to_prompt("Dealer hits..."))
                    self._dealer.hit()
                    continue
                print(f"Dealer stays at {self._dealer._hand_total()}")
                self._dealer.stay()
        
        self.show_results()
        return self._determine_winner()
    
