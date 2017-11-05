from flask import Flask#, session
from flask_ask import Ask, statement, question, session
from enum import Enum
import json
import os
from binascii import hexlify
import jsonpickle

from gameengine import GameEngine

app = Flask(__name__)
ask = Ask(app, "/one")

@ask.launch
def start_skill():
    welcome_message = "Welcome to my app hahahahaha. say... one"
    return question(welcome_message)

@ask.on_session_started
def new_session():
    session.attributes["game_engine"] = jsonpickle.encode(GameEngine())
    print "session started"

# intents that the game will use
@ask.intent("NewGameIntent")
def new_game():
    pass

@ask.intent("GuessIntent")
def guess(UserGuess):
    guess_message = session.attributes["game_engine"].try_guess(UserGuess)
    if guess_message[0] == True:
        session.attributes["game_engine"].next_round()
    return statement(guess_message[1])

@ask.intent("HintIntent")
def hint():
    game_engine = jsonpickle.decode(session.attributes["game_engine"])
    hint_given = game_engine.get_hint()
    #hint_given = session.attributes["game_engine"].get_hint()
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
