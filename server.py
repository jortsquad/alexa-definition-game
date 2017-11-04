from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/one")

def get_one():
    return "one"

@app.route("/")
def homepage():
    return "hi there"

@ask.launch
def start_skil():
    welcome_message = "Welcome to my app hahahahaha. say... one"
    return question(welcome_message)

@ask.intent("OneIntent")
def return_one():
    number = get_one()
    return statement(number)

if __name__ == '__main__':
    app.run(debug=True)
