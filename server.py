from flask import Flask
from flask_ask import Ask, statement, question, session
from enum import Enum
import json
import requests

app = Flask(__name__)
ask = Ask(app, "/one")

class Command(Enum):
    GUESS = 0
    REPEAT_DEFINITION = 1
    HINT = 2
    UNRECOGNIZABLE_INPUT = 3
    CORRECT_WORD = 4
    INCORRECT_WORD = 5
    PASS = 6

def parse_user_command(Enum, user_guess, correct_word):
    # Make Repeat def return a string
    # If user gives up then call reset the loop
    # Guess word just returns the string
    if Enum == Command.GUESS:
        # This method is called and if booleans are passed, decrement/increment score based on the return
        if user_guess == correct_word:
            return Command.CORRECT_WORD;
        elif check_synonyms(user_guess, correct_word) == true:
            return Command.CORRECT_WORD;
        else:
            return Command.INCORRECT_WORD;
        # Check if the user_command matches the word
    elif Enum == Command.REPEAT_DEFINITION:
        # Do API call here with the correct_word and look up the definition
        return definition
    elif Enum == Command.HINT:
        return correct_word[0]
    elif Enum == Command.NEW_WORD:
        return Command.PASS
        # Pick a new word
    else:
        return "I could not understand what you said."
        # Cannot understand the input

def check_synonyms(user_guess, correct_word):
    # Do API call to see the synonyms
    synonym = "Synonym"
    if synonym == user_guess:
        return true
    else:
        return false

@ask.launch
def start_skill():
    welcome_message = "Welcome to my app hahahahaha. say... one"
    return question(welcome_message)

# intents that the game will use
@ask.intent("NewGameIntent")
def new_game():
    pass

@ask.intent("GuessIntent")
def guess(UserGuess):
    print UserGuess
    return statement("Guess")

@ask.intent("HintIntent")
def hint():
    pass

@ask.intent("SkipIntent")
def skip():
    pass

@ask.intent("RepeatIntent")
def repeat():
    pass

@ask.intent("ExitIntent")
def exit():
    pass

# old intents
@app.route("/")
def homepage():
    return "hi there"

if __name__ == '__main__':
    app.run(debug=True)
