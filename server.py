"""Server for park ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
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
        # session['user'] = user

    else:
        crud.create_user(email, password)
        user = crud.get_user_by_email_password(email, password)
        # session['user'] = user
        flash('Welcome to Stars & Dust!')
    
    return redirect('/parks')

# MVP 2.0
@app.route('/logout')
def logout():
    """Logout of website."""

    session.pop("user", None)

    return redirect('/')

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

if __name__ == "__main__":
  connect_to_db(app)
  app.run(debug=True, host='0.0.0.0')

