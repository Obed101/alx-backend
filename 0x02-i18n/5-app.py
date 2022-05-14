#!/usr/bin/env python3
"""This module implements python login and mock"""
from flask import Flask, g, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
app.config['LANGUAGES'] = ["en", "fr"]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.route('/')
def index() -> str:
    """Returns the home page"""
    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> str:
    """Gets the locale and return it"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """Returns a user dictionary or none"""
    user = request.args.get('login_as')
    return users.get(int(user))

@app.before_request
def before_request():
    """returns the default page to display"""
    user = get_user()
    g.user = user


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
