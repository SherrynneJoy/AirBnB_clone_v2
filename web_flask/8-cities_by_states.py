#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State
from models.city import City
from sqlalchemy.orm import close_all_sessions
from os import getenv


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states_list():
    """displays a HTML page"""
    try:
        states = sorted(storage.all(State).values(), key=lambda s: s.name)
        return render_template("8-cities_by_states.html", states=states)
    except Exception as e:
        # Print the exception for debugging
        print(f"Error: {e}")
        return "An error occurred. Please check the logs."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
