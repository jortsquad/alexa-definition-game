import requests
import urllib
import json
import random

from word import Word

class Dictionary():

    def __init__(self,filename):
        self.dictionary = json.load(open(filename))

    # Generates a random word, returned as a Word object
    def get_word(self):
        word_obj = self.dictionary[random.randint(0,len(self.dictionary))]
        return Word(word_obj["word"], word_obj["definition"])
