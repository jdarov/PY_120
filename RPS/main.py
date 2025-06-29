"""
Rock Paper Scissors Game (CLI Version)

This is the main executable script to run a simple 
Rock Paper Scissors game 
between a human player and the computer.

Gameplay:
- The user is prompted to select one of the available moves.
- The computer randomly selects its move.
- The game then displays both moves and announces the winner.

Note:
This version relies on supporting classes from the `rps`
and 'rps_game' module.
"""


from rps_game import RPSGame

def main():
    """
    Implement the main game logic from the RPSGame imported class
    """
    RPSGame().play()

if __name__ == '__main__':
    main()
