"""CRUD operations."""

from sqlalchemy.sql import func

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

    results = db.session.query(Park, func.avg(Rating.score), func.count(Rating.score)).join(Rating).filter(Park.county == county).group_by(Park.park_id)
    parks = []
    
    for park, avg_score, rating_count in results:
        parks.append({'park_id': park.park_id, 
                    'avg_score': round(float(avg_score),2),
                    'rating_count': rating_count,
                    'park_title': park.title,
                    'contract_type': park.contract_type,
                    'latitude': park.latitude,
                    'longitude': park.longitude,
                    'website': park.website,
                    'photo_path': park.photo_path})
    return parks

    # results = db.session.query(Park, func.avg(Rating.score)).join(Rating).filter(Park.county == county).group_by(Park.park_id)
    # parks = []
    
    # for park, avg_score in results:
    #     parks.append({'park_id': park.park_id, 
    #                 'avg_score': round(float(avg_score),2),
    #                 'park_title': park.title,
    #                 'contract_type': park.contract_type,
    #                 'latitude': park.latitude,
    #                 'longitude': park.longitude,
    #                 'website': park.website,
    #                 'photo_path': park.photo_path})
    # return parks

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