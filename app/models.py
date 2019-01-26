from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# User class defines all those who contribute to ShitHappens
class User(Base):
    BASE_RANK       = 'Classic Pooper'
    __tablename__   = 'users'
    id              = Column('user_id', Integer, primary_key=True)
    username        = Column(String(32))
    password        = Column(String(256))
    rank            = Column(String(32))

    # Init func should be called for User creation after new user registers
    def __init__(self, username, hashed_password):
        self.username = username
        self.password = hashed_password
        self.rank     = self.BASE_RANK


# Toilet class defines all toilet objects displayed on the map
class Toilet(Base):
    __tablename__ = 'toilets'
    id = Column('toilet_id', Integer, primary_key=True)
    #rating_id = Column(Integer, ForeignKey('ratings.toilet_id'))
    #rating = relationship('Rating', uselist=False)
    overall_rating = Column(Float)

    longitude = Column(Float)
    latitude = Column(Float)

    def __init__(self, response):
        self.overall_rating = 0.0
        self.longitude = response['longitude']
        self.latitude = response['latitude']


# Rating class defines the various scores given to ech Toilet
class Rating(Base):
    __tablename__ = 'ratings'
    id = Column('rating_id', Integer, primary_key=True)
    toilet_id = Column(Integer, ForeignKey('toilets.toilet_id'))
    toilet = relationship(Toilet)

    cleanliness = Column(Float)

    def __init__(self, toilet_id, response):
        self.toilet_id = toilet_id
        self.cleanliness = response['cleanliness']

# UserRatings stores a table of all the rankings done by a certain User
# This is done to ensure each user can only rate each toilet at most 1 time
#class UserRatings(Base):
#    __tablename__ = 'user-rating'
