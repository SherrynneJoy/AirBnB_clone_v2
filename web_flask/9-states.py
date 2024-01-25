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


@app.route("/states", strict_slashes=False)
def states():
    """displays a html page"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def detailed_states_list(id):
    """displays a HTML page"""
    try:
        state = storage.get(State, id)
        if state:
            cities = sorted(state.cities, key=lambda c: c.name)
            return render_template("9-states.html", state=state, cities=cities)
        else:
            return render_template('not_found.html')
    except Exception as e:
        # Print the exception for debugging
        print(f"Error: {e}")
        return "An error occurred. Please check the logs."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
