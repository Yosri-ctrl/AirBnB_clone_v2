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


@app.route('/c/<string>')
def hello_c(string):
    """C is cool"""
    return "C {}".format(string.replace("_", " "))


@app.route('/python/')
@app.route('/python/<p>')
def hello_python(p="is cool"):
    """Python is cooler"""
    return "Python {}".format(p.replace("_", " "))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
