DEFAULT_SCORE = 10
DEFAULT_HINT_PENALTY = 2
DEFAULT_WRONG_GUESS_PENALTY = 2

# get dictionary
from dictionary import Dictionary
dictionary = Dictionary("dictionary.json")


class GameEngine:

    # Set up gameengine
    def __init__(self):
        self.round = 1
        self.guess = 0
        self.hint = False
        self.total_score = 0
        self.round_score = DEFAULT_SCORE

    def gen_new_word(self):
        self.word_obj = dictionary.get_word()
        print "new word: " + self.word_obj.word

    # Go to next_round
    #returns (isGameStillRunning, total_score, definition)
    def next_round(self):
        if(self.round >= 10):
            return (False, self.total_score, "")
        self.round += 1
        self.gen_new_word()
        self.round_score = DEFAULT_SCORE
        self.guess = 0
        return (True, self.total_score, self.word_obj.definition)

    def try_guess(self, guess_word):
        self.guess += 1
        if self.word_obj.is_similar(guess_word):
            self.total_score += self.round_score
            self.round_score = DEFAULT_SCORE
            return (True, "Right!")
        elif self.guess >= 3:
            past_word = self.word_obj.word
            return (True, "Wrong. The answer is " + past_word)
        else:
            self.round_score -= DEFAULT_WRONG_GUESS_PENALTY
            return (False, "Wrong. Guess again.")

    def get_hint(self):
        if not self.hint:
            hint = True
            self.round_score -= DEFAULT_HINT_PENALTY

        hint_string = "The first letter is " + self.word_obj.word[0] + "... The word has " + str(len(self.word_obj.word)) + " letters"

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
        self.gen_new_word()
