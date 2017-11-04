import requests
import urllib
import json

from word import Word

from secrets import *

RANDOM_WORD_BASE_URL = 'http://api.wordnik.com:80/v4/words.json/randomWord?'
MIN_LENGTH = 5
MAX_LENGTH = 12

class Dictionary():

    def get_random_word(self):
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
        return Word(json_obj['word'])


dic = Dictionary()
print dic.get_random_word()
