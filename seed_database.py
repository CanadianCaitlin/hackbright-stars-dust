"""Script to seed database."""

import os
import json
from random import choice, randint # to create a random score (for MVP)

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load park data from JSON file
with open('data/parks.json') as f:
    park_data = json.loads(f.read())

# Create parks, store them in list so we can use them
# to create fake ratings

parks_in_db = []
for park in park_data:
    title, contract_type, county, latitude, longitude, website, photo_path = (park['title'],
        park['contract_type'],
        park['county'],
        park['latitude'],
        park['longitude'],
        park['website'],
        park['photo_path'])

    db_park = crud.create_park(title,
                                contract_type,
                                county,
                                latitude,
                                longitude,
                                website,
                                photo_path)
    parks_in_db.append(db_park)

# Create 10 users; each user will make 10 ratings
for n in range(100):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)

    for _ in range(100):
        random_park = choice(parks_in_db)
        score = randint(1, 5)

        crud.create_rating(user, random_park, score)