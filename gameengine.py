DEFAULT_SCORE = 10
DEFAULT_HINT_PENALTY = 2
DEFAULT_WRONG_GUESS_PENALTY = 2

# get dictionary
from dictionary import Dictionary
dictionary = Dictionary()


class GameEngine:

    # Set up gameengine
    def __init__(self):
        self.round = 1
        self.guess = 0
        self.hint = False
        self.total_score = 0
        self.round_score = DEFAULT_SCORE
        self.word_obj = dictionary.get_word()
        print self.word_obj.word

    # Go to next_round
    #returns (isGameStillRunning, total_score, definition)
    def next_round(self):
        if(self.round >= 10):
            return (False, self.total_score, "")
        self.round += 1
        self.word_obj = dictionary.get_word()
        self.round_score = DEFAULT_SCORE
        return (True, self.total_score, self.word_obj.definition)

    def try_guess(self, guessWord):
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
            return (False, "Wrong. Guess again.")

    def get_hint(self):
        if not self.hint:
            hint = True
            self.round_score -= DEFAULT_HINT_PENALTY

        hint_string = "The first letter is" + self.word_obj.word[0] + "... The length is " + str(len(self.word_obj.word))

        return hint_string

    def skip(self):
        return "The answer is " + self.word_obj.word

    def repeat(self):
        return self.word_obj.definition

    def reset(self):
        self.round = 1
        self.guess = 0
        self.hint = False
        self.total_score = 0
        self.round_score = DEFAULT_SCORE
        self.word_obj = dictionary.get_word()
