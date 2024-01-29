#!/usr/bin/python3
"""Script that executes an app using Flask framework."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function to display 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function to display 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Function to display 'C' followed by the provided text."""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Function to display 'Python' followed by the provided text."""
    if text != 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Function to display if the provided value is a number."""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Function to render a template with the provided number."""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
