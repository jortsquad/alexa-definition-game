from flask import Flask#, session
from flask_ask import Ask, statement, question, session
from enum import Enum
import json
import os
from binascii import hexlify

from gameengine import GameEngine

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

@ask.on_session_started
def new_session():
    session.attributes["game_engine"] = GameEngine()
    print "session started"

# intents that the game will use
@ask.intent("NewGameIntent")
def new_game():
    pass

@ask.intent("GuessIntent")
def guess(UserGuess):
    guess_message = session.attributes["game_engine"].guess(UserGuess)
    if guess_message[0] == True:
        session.attributes["game_engine"].next_round()
    return statement(guess_message[1])

@ask.intent("HintIntent")
def hint():
    hint_given = session.attributes["game_engine"].hint()
    return statement(hint_given)

@ask.intent("SkipIntent")
def skip():
    skip_message = session.attributes["game_engine"].skip()
    session.attributes["game_engine"].next_round()
    return statement(skip_message)

@ask.intent("RepeatIntent")
def repeat():
    repeat_message = session.attributes["game_engine"].repeat()
    return statement(repeat_message)

@ask.intent("ExitIntent")
def exit():
    pass

# old intents
@app.route("/")
def homepage():
    return "hi there"

if __name__ == '__main__':
    app.secret_key = hexlify(os.urandom(24))
    app.run(debug=True)
