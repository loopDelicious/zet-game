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


# select random 12 cards to display that includes at least 1 zet
# keep track of zets found and remaining
# verify if zet selected is from the remaining zets

@app.route('/generate_display')
def generate_display():
    """Create the initial panel of cards to display."""

    deck = Deck()

    zet_deck = deck.shuffle().deal()

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