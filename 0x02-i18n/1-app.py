#!/usr/bin/env python3
"""This module implements python flask_babel"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
LANGUAGES = ["en", "fr"]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'


@app.route('/')
def index() -> str:
    """Returns the home page"""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run()
