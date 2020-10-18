"""CRUD operations."""

from model import db, User, Park, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return all users."""

    return User.query.all()

# MVP 2.0
def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)

# MVP 2.0
def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_by_email_password(email, password):
    """Return a user by email and password."""

    return User.query.filter(User.email == email, User.password == password).first()

def create_rating(user, park, score):
    """Create and return a new rating."""

    rating = Rating(user=user, park=park, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_park_by_county(county):
    """Return list of parks within selected county."""

    return Park.query.filter(Park.county == county)

def create_park(title, contract_type, county, latitude, longitude, website, photo_path):
    """Create and return a new park."""

    park = Park(title=title,
                contract_type=contract_type,
                county=county,
                latitude=latitude,
                longitude=longitude,
                website=website,
                photo_path=photo_path)

    db.session.add(park)
    db.session.commit()

    return park


if __name__ == '__main__':
    from server import app
    connect_to_db(app)