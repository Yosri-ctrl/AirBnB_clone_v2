#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """method returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """method returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """method returns C + text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """method returns python + text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """method returns number"""
    return '{} is a number'.format(int(n))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
