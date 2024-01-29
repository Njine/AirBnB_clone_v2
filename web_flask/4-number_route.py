#!/usr/bin/python3
"""Runs a simple Flask application with specified routes."""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """Route to display 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb():
    """Route to display 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """Route to display 'C' followed by the provided text."""
    return "C " + text.replace("_", " ")


@app.route("/python")
@app.route("/python/<text>")
def python_is_fun(text="is cool"):
    """Route to display 'Python' followed by the provided text."""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>")
def is_number(n):
    """Route to display if the provided value is a number."""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
