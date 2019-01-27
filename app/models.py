from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# User class defines all those who contribute to ShitHappens
class User(Base):
    RANKS           = ['Novice Pooper', 'Junior Pooper', 'Experienced Pooper', 'Advanced Pooper', 'Elite Pooper', 'Presidential Pooper', 'Supreme Pooper']
    __tablename__   = 'users'
    id              = Column('user_id', Integer, primary_key=True)
    username        = Column(String(32))
    password        = Column(String(256))
    rank            = Column(String(32))
    rating_count    = Column(Integer)

    # Init func should be called for User creation after new user registers
    def __init__(self, username, hashed_password):
        self.username = username
        self.password = hashed_password
        self.rank = self.RANKS[0]
        self.rating_count = 0

    # Update this users rank through the list
    def update_rank(self):
        if self.rank != 'Supreme Pooper':
            self.rank = RANKS[RANKS.index(self.rank) + 1]


# Toilet class defines all toilet objects displayed on the map
class Toilet(Base):
    __tablename__ = 'toilets'
    id = Column('toilet_id', Integer, primary_key=True)
    title = Column(String(32))
    description = Column(String(256))

    rating_count = Column(Integer)
    overall_rating = Column(Float)
    longitude = Column(Float)
    latitude = Column(Float)

    def __init__(self, response):
        self.overall_rating = 0.0
        self.rating_count = 0
        self.title = response['title']
        self.description = response['description']
        self.longitude = response['longitude']
        self.latitude = response['latitude']


# Rating class defines the various scores given to ech Toilet
class Rating(Base):
    __tablename__ = 'ratings'
    id = Column('rating_id', Integer, primary_key=True)
    toilet_id = Column(Integer, ForeignKey('toilets.toilet_id'))
    toilet = relationship(Toilet)

    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship(User)

    cleanliness = Column(Integer)
    smell_rating = Column(Integer)
    number_of_stalls = Column(Integer)
    artwork = Column(Integer)
    toilet_paper_quality = Column(Integer)
    flush_pressure = Column(Integer)

    has_toilet_paper = Column(Boolean)
    has_handicap_stall = Column(Boolean)
    has_seat_cover = Column(Boolean)
    is_gender_neutral = Column(Boolean)
    has_baby_station = Column(Boolean)
    has_hook = Column(Boolean)

    comment = Column(String(256))

    def __init__(self, user_id, toilet_id, response):
        self.user_id = user_id
        self.toilet_id = toilet_id
        self.cleanliness = response['cleanliness']
        self.smell_rating = response['smell_rating']
        self.number_of_stalls = response['number_of_stalls']
        self.artwork = response['artwork']
        self.toilet_paper_quality = response['toilet_paper_quality']
        self.flush_pressure = response['flush_pressure']

        self.has_toilet_paper = response['has_toilet_paper']
        self.has_handicap_stall = response['has_handicap_stall']
        self.has_seat_cover = response['has_seat_cover']
        self.has_baby_station = response['has_baby_station']
        self.is_gender_neutral = response['is_gender_neutral']
        self.has_hook = response['has_hook']

# UserRatings stores a table of all the rankings done by a certain User
# This is done to ensure each user can only rate each toilet at most 1 time
#class UserRatings(Base):
#    __tablename__ = 'user-rating'
#    id = Column(Integer)
#    user_id = Column(Integer, ForeignKey('users.user_id'))
#    user = relationship(User)
#
#    toilet_id = Column(Integer, ForeignKey('toilets.toilet_id'))
#    toilet = relationship(Toilet)


