class Word:
    def soundex(self, name):
        length = 4
        digits = '01230120022455012623010202'
        sndx = ''
        fc = ''

        for c in name.upper():
            if c.isalpha():
                if not fc: fc = c
                d = digits[ord(c)-ord('A')]
                if not sndx or (d != sndx[-1]):
                    sndx += d

        sndx = fc + sndx[1:]

        sndx = sndx.replace('0','')

        return (sndx + ('0' * length))[:length]

    def __init__(self, word, definition):
        self.word = word
        self.definition = definition

    def __str__(self):
        return self.word + ': ' + self.definition

    def is_similar(self, other_word):
        if other_word.lower().strip() == self.word.lower().strip():
            return True
        return False
