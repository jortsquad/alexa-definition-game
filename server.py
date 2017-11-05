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
    game_engine = jsonpickle.decode(session.attributes["game_engine"])
    welcome_message = "Welcome to the definition game! The first definition is..... " + game_engine.word_obj.definition
    return question(welcome_message)

@ask.on_session_started
def new_session():
    engine = GameEngine()
    engine.gen_new_word()
    session.attributes["game_engine"] = jsonpickle.encode(engine)

    print "session started"

# intents that the game will use
@ask.intent("NewGameIntent")
def new_game():
    print 'new game'
    new_game_engine = GameEngine()
    new_game_engine.gen_new_word()
    new_definition = new_game_engine.word_obj.definition
    session.attributes["game_engine"] = jsonpickle.encode(new_game_engine)
    return question("This is a new game. The first definition is...... " + new_definition)

@ask.intent("GuessIntent")
def guess(UserGuess):
    print UserGuess
    game_engine = jsonpickle.decode(session.attributes["game_engine"])

    guess_message = game_engine.try_guess(UserGuess)

    if guess_message[0] == True:
        next_round_tuple = game_engine.next_round()
        if next_round_tuple[0]:
            score = next_round_tuple[1]
            new_definition = next_round_tuple[2]

            session.attributes["game_engine"] = jsonpickle.encode(game_engine)
            return statement(guess_message[1] + "... You have " + str(score) + " points. New word definition is....." + new_definition)
        else:
            pass


    session.attributes["game_engine"] = jsonpickle.encode(game_engine)

    return question(guess_message[1])

@ask.intent("HintIntent")
def hint():
    game_engine = jsonpickle.decode(session.attributes["game_engine"])

    hint_given = game_engine.get_hint()

    session.attributes["game_engine"] = jsonpickle.encode(game_engine)
    return question(hint_given)

@ask.intent("SkipIntent")
def skip():
    game_engine = jsonpickle.decode(session.attributes["game_engine"])

    skip_message = game_engine.skip()

    next_round_tuple = game_engine.next_round()
    if next_round_tuple[0]:
        score = next_round_tuple[1]
        new_definition = next_round_tuple[2]

        session.attributes["game_engine"] = jsonpickle.encode(game_engine)
        return question(skip_message + "... You have " + str(score) + " points. New word definition is....." + new_definition)
    else:
        pass

@ask.intent("RepeatIntent")
def repeat():
    game_engine = jsonpickle.decode(session.attributes["game_engine"])

    repeat_message = game_engine.repeat()

    session.attributes["game_engine"] = jsonpickle.encode(game_engine)
    return question(repeat_message)

@ask.intent("ExitIntent")
def exit():
    print 'exiting'
    pass


# old intents
@app.route("/")
def homepage():
    return "hi there"

if __name__ == '__main__':
    app.secret_key = hexlify(os.urandom(24))
    app.run(debug=True)
