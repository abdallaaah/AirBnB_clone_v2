#!/usr/bin/python3
""" 1. Script to start a Flask web application with 2 commands """

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """this is the index page for the app"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """this is the index page for the app"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """this is to dislay txt after the slash and replace coma with text"""
    return f"c {escape(text.replace('_',' '))}"


if __name__ == "__main__":
    """the first point the app start from"""
    app.run(host='0.0.0.0', port=5000, debug=True)
