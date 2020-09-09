#!/usr/bin/python3
"""Start a flak application"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    """print Hello HBNB"""
    return ("Hello HBNB!")


@app.route("/hbnb")
def hello_HBNB():
    """print HBNB"""
    return ("HBNB")


@app.route('/c/<string:s>')
def hello_c(s):
    return "C {}".format(s.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
