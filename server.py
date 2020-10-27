"""Server for park ratings app."""
import json

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
import requests
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/login', methods=['POST'])
def login():
    """Login to website or create new account."""

    email = request.args.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email_password(email, password)

    if user:
        flash('Welcome back to Stars & Dust!')
        session['user'] = user.user_id

    else:
        crud.create_user(email, password)
        user = crud.get_user_by_email_password(email, password)
        session['user'] = user.user_id
        flash('Welcome to Stars & Dust!')
    
    return redirect('/parks')

# MVP 2.0
@app.route('/logout')
def logout():
    """Logout of website."""

    session.pop("user", None)

    return redirect('/')

@app.route('/parks', methods=['GET','POST'])
def search_parks():
    """View parks based on user criteria submission."""

    if request.method == "POST":
        county = request.form.get('county')
        parks = crud.get_park_by_county(county)
        
        return render_template('parkresults.html', 
                               county=county, 
                               parks=parks)

    else:
        return render_template('parks.html')

@app.route('/parks_data', methods=['GET'])
def parks_data():
    """Get a JSON view of the parks."""
    county = request.args.get('county')
    parks = crud.get_park_by_county(county)
    parks_lst = {'parks': [{'county': park.county,
                            'lng': park.longitude,
                            'lat': park.latitude} for park in parks]}
    
    return jsonify(parks_lst)


# MVP 2.0
@app.route('/trails')
def search_trails():
    """View trails."""

    return render_template('trails.html')

# MVP 2.0
@app.route('/stargazing')
def stargazing_search():
    """View stargazing locations."""

    return render_template('stargazing.html')

if __name__ == "__main__":
  connect_to_db(app)
  app.run(debug=True, host='0.0.0.0')

