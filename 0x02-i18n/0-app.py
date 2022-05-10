#!/usr/bin/env python3
"""This module starts python flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Returns the home page"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(index())