"""Zet card game."""

import sqlalchemy
from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect

import os
import json
import requests
import random


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = os.environ["FLASK_SECRET_KEY"]

# Raise an error if you use an undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


count = [1,2,3]
color = [Red, Blue, Green]
shape = [circle, square, bone]
fill = [speckle, solid, empty]

# card = [0,1,2,2] count 1, color blue, shape bone, fill empty

# select random 12 cards to display that includes at least 1 zet
# keep track of zets found and remaining
# verify if zet selected is from the remaining zets
def is_zet(x, y, z):
    """Determine if zet fulfills criteria of all the same OR all different on 4 criteria:  count, color, shape, fill)"""

    if not (x[0] == y[0] == z[0]) | (x[0] != y[0] != z[0]):
        return False  # count

    if not (x[1] == y[1] == z[1]) | (x[1] != y[1] != z[1]):
        return False  # color

    if not (x[2] == y[2] == z[2]) | (x[2] != y[2] != z[2]):
        return False  # shape

    if not (x[3] == y[3] == z[3]) | (x[3] != y[3] != z[3]):
        return False  # fill


    # if defining card class with feature methods 
    if not (x.count == y.count == z.count) | (x.count != y.count != z.count):
        return False

    if not (x.color == y.color == z.color) | (x.color != y.color != y.color):
        return False

    if not (x.shape == y.shape == z.shape) | (x.shape != y.shape != z.shape):
        return False

    if not (x.fill == y.fill == z.fill) | (x.fill != y.fill != z.fill):
        return False

    return True


@app.route('/create_deck')
def create_deck():
    """Create an initial deck of 81 cards where each feature combination occurs precisely once in the deck."""


@app.route('/generate_display')
def generate_display():
    """Create the initial panel of cards to display."""

    with open('seed.txt', 'r') as f:
        # create a list of cards to display
        deck = f.readlines()

    need_new_cards = True

    while need_new_cards:

        card_batch = []

        # generate an arry of 12 random cards
        for i in range(1,12):
            card = random.choice(deck) # random card
            card_batch.append()

        # if card_batch contains at least 1 zet, maintain
        #   need_new_cards = False
        # else redraw

    return card_batch


@app.route('/favicon.ico')
def favicon():
    """Zet cards favicon"""

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon-th.ico', mimetype='image/vnd.microsoft.icon')



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()
    # app.run(host='0.0.0.0')