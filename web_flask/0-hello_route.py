#!/usr/bin/python3
"""Start a flak application"""
from flask import Flask


app = Flask(__name__)
@app.route("/")
def hello():
    """print Hello HBNB"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run()
