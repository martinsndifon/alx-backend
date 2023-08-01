#!/usr/bin/env python3
"""ALX SE flask app"""
from flask import Flask, render_template
from flask_babel import Babel
from config import Config

app =  Flask(__name__)
app.config.from_object(Config)


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Initialize and set default config for babel
babel = Babel(app, locale_selector=get_locale, default_timezone='UTC')

@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """prints hello world"""
    return render_template('1-index.html')

if __name__ == "__main__":
    """main entry"""
    app.run(host='0.0.0.0', port='5000', threaded=True)
