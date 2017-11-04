DEFAULT_SCORE = 10
DEFAULT_HINT_PENALTY = 2
DEFAULT_WRONG_GUESS_PENALTY = 2

from dictionary import Dictionary

dictionary = Dictionary()

class GameEngine:

    def __init__(self):
        self.round = 1
        self.guess = 0
        self.hint = False
        self.total_score = 0
        self.round_score = DEFAULT_SCORE
        self.word_obj = dictionary.get_word()

    def next_round(self):
        if(self.round >= 10):
            return (False, total_score, "")
        self.round += 1
        self.word_obj = dictionary.get_word()
        self.round_score = DEFAULT_SCORE
        return (True, total_score,word_obj.definition)

    def guess(self, guessWord):
        self.guess += 1
        if self.word == guessWord:
            self.total_score += self.round_score
            self.round_score = DEFAULT_SCORE
            return (True, "Right!")
        if self.guess >= 3:
            past_word = self.word_obj.word
            return (True, "Wrong. The answer is " + past_word)
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
        return "The answer is " + self.word_obj.word

    def repeat(self):
        return word_obj.definition

    def reset(self):
        self.round = 1
        self.guess = 0
        self.hint = False
        self.total_score = 0
        self.round_score = DEFAULT_SCORE
        self.word_obj = dictionary.get_word()
