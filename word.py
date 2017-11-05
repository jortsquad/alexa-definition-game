from jaccard_coefficient import jaccard, ngrams
from edit_distance import edit_distance

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
        soundex_max_threshold = 2
        jaccard_min_threshold = 0.4

        soundex_edit_distance = edit_distance(self.soundex(self.word.lower()), self.soundex(other_word))
        jaccard_coeff = jaccard(3, self.word.lower(), other_word)

        if other_word.lower() == self.word.lower() or soundex_edit_distance <= soundex_max_threshold or jaccard_coeff > jaccard_min_threshold:
            return True
        for synonym in self.synonyms:
            soundex_edit_distance = edit_distance(self.soundex(synonym.lower()), self.soundex(other_word))
            jaccard_coeff = jaccard(3, synonym.lower(), other_word)

            if synonym.lower() == self.word.lower() or soundex_edit_distance <= soundex_max_threshold or jaccard_coeff > jaccard_min_threshold:
                return True

        return False
