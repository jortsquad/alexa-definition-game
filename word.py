class Word:

    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        self.synonyms = []

    def __str__(self):
        syn_text = ''
        for i in range(len(self.synonyms)):
            if i > 0:
                syn_text += ', '
            syn_text += self.synoynms[i]
        return self.word + ': ' + self.definition + ' [' + syn_text + ']'
