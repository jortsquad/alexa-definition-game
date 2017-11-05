import requests
import urllib
import json

from word import Word

from secret import *


RANDOM_WORD_BASE_URL = 'http://api.wordnik.com:80/v4/words.json/randomWord?'
WORD_DEFN_BASE_URL = 'http://api.wordnik.com:80/v4/word.json/%s/definitions?'
WORD_RELATIONSHIPS_BASE_URL = 'http://api.wordnik.com:80/v4/word.json/%s/relatedWords?'
MIN_LENGTH = 5
MAX_LENGTH = 12

class Dictionary():

    # Generates a random word, returned as a Word object
    def get_word(self):
        word = ''
        definition = None
        synonyms = []
        while not self._is_word_valid(word, definition):
            word = self._get_random_word()
            definition = self._get_word_definition(word)
        synonyms = self._get_word_synonyms(word)
        return Word(word, definition, synonyms)

    # Determines whether or not a given word (and definition) is valid
    def _is_word_valid(self, word, definitions):
        if definition is None:
            return False
        if len(definition) > 3 and defintion.lower()[:3] == 'see':
            return False
        if word.lower() in definition.lower():
            return False
        if len(word) == 0:
            return False
        if word[0].isupper():
            return False
        if 'plural' in definition.lower():
            return False
        return True

    # Obtains a random word as a string from the Wordnik API
    def _get_random_word(self):
        params = {
            'hasDictionaryDef' : 'true',
            'minCorpusCount' : 0,
            'maxCorpusCount' : -1,
            'minDictionaryCount' : 1,
            'maxDictionaryCount' : -1,
            'includePartOfSpeech' : 'noun',
            'minLength' : MIN_LENGTH,
            'maxLength' : MAX_LENGTH,
            'api_key' : WORDNIK_API_KEY
        }

        url = RANDOM_WORD_BASE_URL + urllib.urlencode(params)
        response = requests.get(url)
        json_obj = json.loads(response.text)
        return json_obj['word']

    # Gets the definition of a given word from the Wordnik API
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

    # Gets a list of synonyms for a given word from the Wordnik API
    def _get_word_synonyms(self, word):
        params = {
            'includeRelated' : 'true',
            'relationshipTypes' : 'synonym',
            'limitPerRelationshipType' : 10,
            'api_key' : WORDNIK_API_KEY
        }

        url = (WORD_RELATIONSHIPS_BASE_URL % word) + urllib.urlencode(params)
        response = requests.get(url)
        json_obj = json.loads(response.text)

        if len(json_obj) < 1:
            return []
        synonyms = json_obj[0]['words']
        return synonyms
