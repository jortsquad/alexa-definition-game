class Word:

    def __init__(self, word, definition, synonyms):
        self.word = word
        self.definition = definition
        self.synonyms = synonyms

    def __str__(self):
        syn_text = ''
        for i in range(len(self.synonyms)):
            if i > 0:
                syn_text += ', '
            syn_text += self.synonyms[i]
        return self.word + ': ' + self.definition + ' [' + syn_text + ']'

    def is_similar(self, other_word):
        if other_word.lower() == self.word.lower():
            return True
        for synonym in self.synonyms:
            if synonym.lower() == self.word.lower():
                return True
        return False
