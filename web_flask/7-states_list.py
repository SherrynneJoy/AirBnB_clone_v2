#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """displays a HTML page"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
