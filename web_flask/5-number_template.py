#!/usr/bin/python3
""" 1. Script to start a Flask web application with 2 commands """

from flask import Flask, render_template
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
    return f"C {escape(text.replace('_',' '))}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_text_python(text='is cool'):
    """this is to display txt after the slash with defualt value python"""
    return f"Python {escape(text.replace('_',' '))}"


@app.route('/number/<int:num>', strict_slashes=False)
def display_integet_numbers(num):
    """this is to display number integers"""
    if isinstance(num, int):
        return f"{num} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def return_number_Template(n):
    """this is to render template with dynamic number"""
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


if __name__ == "__main__":
    """the first point the app start from"""
    app.run(host='0.0.0.0', port=5000, debug=True)
