#!/usr/bin/python3
"""the entry point"""
from . import app


if __name__ == "__main__":
    """the first point the app start from"""
    app.run(host='0.0.0.0', port=5000)


@app.route('/', strict_slashes=False)
def index():
    """this is the index page for the app"""
    return "Hello HBNB!"
