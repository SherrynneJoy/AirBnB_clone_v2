#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, abort, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def display_python(text="is cool"):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<n>", strict_slashes=False)
def is_number(n):
    try:
        n = int(n)
        return f'{n} is a number'
    except ValueError:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def render_number(n):
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except ValueError:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def even_or_odd(n):
    try:
        n = int(n)
        odd_even = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', n=n, odd_even=odd_even)
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
