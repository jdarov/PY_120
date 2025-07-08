class Game:
    count = 0
    def __init__(self, game, player_name):
        self._game = game
        self.player_name1 = player_name
        Game.count += 1
    
    def play(self):
        return f'Start the {self._game} game!'
    @property
    def player_name(self):
        return self.player_name1
    def play(self):
        return 'Start the game!'

class Bingo(Game):
    def __init__(self, game, player_name):
        super().__init__(game, player_name)

class Scrabble(Game):
    def __init__(self, game, player_name1, player_name2):
        super().__init__(game, player_name1)
        self.player_name2 = player_name2

        @property
        def player_name(self):
            raise AttributeError("Scrabble object has no attribue 'player_name")

bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'


