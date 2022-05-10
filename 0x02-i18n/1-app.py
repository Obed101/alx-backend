#!/usr/bin/env python3
"""This module implements python flask_babel"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
LANGUAGES = ["en", "fr"]



@app.route('/')
def index():
    """Returns the home page"""
    return render_template("0-index.html")

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(index())
# add to you main app code
