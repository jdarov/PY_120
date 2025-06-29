class RulesMixIN:
    def _display_rules(self):
        """
        A mixin for displaying the rules in a clean
        nice readable way for the user.
        Rcok, Paper, Scissors, Lizard, Spock
        """
        print("=" * 50)
        print("HOW TO PLAY: Rock, Paper, Scissors, Lizard, Spock")
        print("=" * 50)
        print("Each player chooses one of the following options:")
        print("  - Rock")
        print("  - Paper")
        print("  - Scissors")
        print("  - Lizard")
        print("  - Spock\n")
        
        print("The rules are simple:")
        print("     Rock crushes Scissors and crushes Lizard")
        print("     Paper covers Rock and disproves Spock")
        print("     Scissors cuts Paper and decapitates Lizard")
        print("     Lizard eats Paper and poisons Spock")
        print("     Spock smashes Scissors and vaporizes Rock\n")
        
        print("First to 5 wins is the GRAND WINNER!\n")
        print("=" * 50)
        print()
