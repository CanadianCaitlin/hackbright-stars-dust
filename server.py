"""Server for park ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
import requests
import xml.etree.ElementTree as et # converts XML to Python object
# from model import connect_to_db
# import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/parks')
def search_parks():
    """View parks."""

    return render_template('parks.html')

# MVP 2.0
@app.route('/trails')
def search_trails():
    """View homepage."""

    return render_template('trails.html')

# MVP 2.0
@app.route('/stargazing')
def stargazing_search():
    """View homepage."""

    return render_template('stargazing.html')

# To Do: add functionality
# @app.route('/login')
# def homepage():
#     """Login to website."""
#     pass

if __name__ == "__main__":
#   connect_to_db(app)
  app.run(debug=True, host='0.0.0.0')

