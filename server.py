"""Zet card game."""

import sqlalchemy
from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, Response
from model import Card, Deck


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
    """Create the initial panel of 12 cards to display."""

    card_batch = Deck().shuffle().newDeal()
    import pdb; pdb.set_trace()

    # need_new_cards = True

    # while need_new_cards:

    #     card_batch = []

    #     # generate an array of 12 random cards
    #     for i in range(1,12):
    #         card = random.choice(deck) # random card
    #         card_batch.append(card)

    #     # if card_batch contains at least 1 zet, maintain
    #     #   need_new_cards = False
    #     # else redraw
    #     card_batch

    return Response(json.dumps(card_batch),  mimetype='application/json')


@app.route('/favicon.ico')
def favicon():
    """Zet cards favicon"""

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon-th.ico', mimetype='image/vnd.microsoft.icon')



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    app.run()
    # app.run(host='0.0.0.0')