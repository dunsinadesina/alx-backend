#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask
from flask import request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


    # intstantiate application object
    app = Flask(__name__)
    app.config.from_object(Config)

    # wrap the app with Babel
    babel = Babel(app)


    @babel.localeselector
    def get_locale():
        """gets locale from request object"""
        return request.accept_languages.best_match(app.config['LANGUAGES'])


    @app.route('/', strict_slashes=False)
    def index():
        """renders html template"""
        return render_template('2-index.html')


    if __name__ == '__main__':
        app.run()
