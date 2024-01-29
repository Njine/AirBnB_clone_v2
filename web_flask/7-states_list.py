#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """ Display a list of states """
    states = storage.all(State)
    state_dict = {state.id: state.name for state in states.values()}
    return render_template('7-states_list.html', Table="States", items=state_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
