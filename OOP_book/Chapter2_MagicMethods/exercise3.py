class Candidate:
    candidate_votes = 0
    total_votes = 0

    def __init__(self, name):
        self._name = name
        self._votes = 0

    @property
    def votes(self):
        return self._votes
    
    @votes.setter
    def votes(self, number_of_votes):
        self._votes = number_of_votes

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def percentage(self):
        return (self.votes/Candidate.total_votes) * 100
    
    def __iadd__(self, increment):
        self.votes += increment
        Candidate.total_votes += increment
        return self
    
    def __str__(self):
        if self.votes > 1:
            return f'{self._name}: {self._votes} votes'
        return f'{self.name}: {self.votes} vote'

class Election:

    def __init__(self, candidates):
        if not isinstance(candidates, (list,set)):
            raise ValueError("You must input a list of names to add votes")
        self._candidates = candidates
    
    def results(self):
        winner = None
        highest_votes = 0
        for candidate in self._candidates:
            if not isinstance(candidate, Candidate):
                raise ValueError("The candidate is not defined as a Candidate")
            print(f'{candidate}')
            if candidate.percentage > highest_votes:
                highest_votes = candidate.percentage
                winner = candidate
        print(f'\n{winner.name} won: {winner.percentage:.1f}% of votes')

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()