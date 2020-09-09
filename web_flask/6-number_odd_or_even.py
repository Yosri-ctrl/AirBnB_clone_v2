#!/usr/bin/python3
"""Start a flak application"""
from flask import Flask, render_template
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


@app.route('/number/<int:num>')
def number(num):
    """Check if it is a number"""
    if type(num) == int:
        return "{} is a number".format(num)


@app.route('/number_template/<int:num>')
def number_template(num):
    return render_template('5-number.html', num=num)


@app.route('/number_odd_or_even/<int:num>')
def number_odd_or_even(num):
    if num % 2 == 0:
        string = "even"
    else:
        string = "odd"
    return render_template('6-number_odd_or_even.html', num=num, type=string)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
