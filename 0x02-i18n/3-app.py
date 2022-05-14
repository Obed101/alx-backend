#!/usr/bin/env python3
"""This module implements python flask_babel"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
app.config['LANGUAGES'] = ["en", "fr"]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'


@app.route('/')
def index() -> str:
    """Returns the home page"""
    return render_template("3-index.html")


@babel.localeselector
@app.route('/locale')
def get_locale() -> str:
    """Gets the locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
