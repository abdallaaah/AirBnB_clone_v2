#!/usr/bin/python3
""" 1. Script to start a Flask web application with 2 commands """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """this is the index page for the apppp"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """this is the index page for the app"""
    return "HBNB"


if __name__ == "__main__":
    """the first point the app start from"""
    app.run(host='0.0.0.0', port=5000, debug=True)
