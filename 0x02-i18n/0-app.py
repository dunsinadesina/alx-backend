#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    simply outputs “Welcome to Holberton” as page title
    (<title>) and “Hello world” as header (<h1>)
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
