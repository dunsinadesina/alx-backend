#!/usr/bin/python3
"""basic flask app"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


    #instantitate application object
    app = Flask(__name__)
    app.config.from_object(Config)


    #wrap application with babel
    babel = Babel(app)


    @app.route('/', strict_slashes=False)
    def index():
        """renders basic html template"""
        return render_template('1-index.html')


    if __name__ == '__main__':
        app.run()
