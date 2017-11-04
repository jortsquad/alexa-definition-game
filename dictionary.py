import requests
import urllib
import json

from word import Word

from secrets import *

#http://api.wordnik.com:80/v4/word.json/magic/definitions?limit=200&includeRelated=true&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5

RANDOM_WORD_BASE_URL = 'http://api.wordnik.com:80/v4/words.json/randomWord?'
WORD_DEFN_BASE_URL = 'http://api.wordnik.com:80/v4/word.json/%s/definitions?'
MIN_LENGTH = 5
MAX_LENGTH = 12

class Dictionary():

    def get_word(self):
        word = ''
        definition = None
        while not self._is_word_valid(word, definition) or definition is None:
            word = self._get_random_word()
            definition = self._get_word_definition(word)
        return Word(word, definition)

    # Determines whether or not a given word (and definition) is valid
    def _is_word_valid(self, word, definition):
        if len(word) == 0:
            return False
        if word[0].isupper():
            return False
        if 'plural' in definition.lower():
            return False
        return True

    def _get_random_word(self):
        params = {
            'hasDictionaryDef' : 'true',
            'minCorpusCount' : 0,
            'maxCorpusCount' : -1,
            'minDictionaryCount' : 1,
            'maxDictionaryCount' : -1,
            'minLength' : MIN_LENGTH,
            'maxLength' : MAX_LENGTH,
            'api_key' : WORDNIK_API_KEY
        }

        url = RANDOM_WORD_BASE_URL + urllib.urlencode(params)
        response = requests.get(url)
        json_obj = json.loads(response.text)
        return json_obj['word']

    def _get_word_definition(self, word):

        params = {
            'limit' : 200,
            'includeRelated' : 'true',
            'useCanonical' : 'false',
            'includeTags' : 'false',
            'api_key' : WORDNIK_API_KEY
        }
        url = (WORD_DEFN_BASE_URL % word) + urllib.urlencode(params)
        response = requests.get(url)
        json_obj = json.loads(response.text)

        if len(json_obj) < 1:
            return None

        first_definition = json_obj[0]['text']
        return first_definition



dic = Dictionary()
print dic.get_word()
