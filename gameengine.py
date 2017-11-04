DEFAULT_SCORE = 10
DEFAULT_HINT_PENALTY = 2
DEFAULT_WRONG_GUESS_PENALTY = 2


class GameEngine:

    def __init__(self):
        self.round = 1
        self.guess = 0
        self.hint = False
        self.total_score = 0
        self.round_score = DEFAULT_SCORE

    def new_word(self):
        pass

    def guess(self, guessWord):
        self.guess += 1
        if self.word == guessWord:
            self.total_score += self.round_score
            self.round_score = DEFAULT_SCORE
            return (True, "Right!")
        if self.guess >= 3:
            return (True, "Wrong. The answer is " + self.word)
        else:
            self.round_score -= DEFAULT_WRONG_GUESS_PENALTY
            return (False, "Wrong")

    def hint(self):
        if not self.hint:
            hint = True
            self.round_score -= DEFAULT_HINT_PENALTY
        hint_string = "The first letter is" + word_obj.word[0]
        + "... The length is " + len(word_obj.word)
        return hint_string

    def skip(self):
        self.round += 1
        self.word_obj

    def repeat(self):
        return word_obj.definition

    def reset(self):
        self.round = 1
        self.guess = 0
        self.hint = False
        self.total_score = 0
        self.round_score = DEFAULT_SCORE
