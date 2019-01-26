from sqlalchemy import Column, Integer, Float, String
from .database import Base

# User class defines all those who contribute to ShitHappens
class User(Base):
    BASE_RANK       = 'Classic Pooper'
    __tablename__   = 'users'
    id              = Column('user_id', Integer, primary_key=True)
    username        = Column(String(32))
    rank            = Column(String(32))

    # Init func should be called for User creation after new user registers
    def __init__(self, response):
        self.username = response['username']
        self.rank     = BASE_RANK



# Toilet class defines all toilet objects displayed on the map
class Toilet(Base):
    __tablename__ = 'toilets'
    id = Column('toilet_id', Integer, primary_key=True)
    rating = Column(Rating)

    longitude = Column(Float)
    latitude = Column(Float)

# Rating class defines the various scores given to ech Toilet
class Rating(Base):
    overall = float
    cleanliness = float



