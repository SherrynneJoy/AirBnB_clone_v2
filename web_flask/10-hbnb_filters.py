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


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display a HTML page like 6-index.html."""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
