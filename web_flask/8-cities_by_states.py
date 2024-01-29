#!/usr/bin/python3
""" Script that utilizes Flask framework to run an application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """ Close session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_html():
    """ Display cities grouped by states """
    states = storage.all(State)
    cities_by_states = {}
    for state in states.values():
        cities_by_states[state] = state.cities
    return render_template('8-cities_by_states.html',
                           Table="States and their Cities",
                           cities_by_states=cities_by_states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
