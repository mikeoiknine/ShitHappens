from .database import db_session
from .models import Toilet, Rating, User

def update_toilet_rank(toilet_id, rating):
    toilet = db_session.query(Toilet).filter(Toilet.id == toilet_id).first()
    ratings = db_session.query(Rating).filter(Rating.toilet_id == toilet_id).all()

    if toilet is None:
        return "Error: invalid toilet"

    rating_count = 1

    # Algorithm is super complex, add all numerical values
    # add +5 for every boolean that is true, 0 if false then divide
    # by the magic number
    score = 0
    magic_number = 8

    # Add the current rating being made to this toilet
    score += int(rating.cleanliness)
    score += int(rating.cleanliness)
    score += int(rating.smell_rating)
    score += int(rating.artwork)
    score += int(rating.toilet_paper_quality)
    score += int(rating.flush_pressure)
    score -= int(rating.number_of_stalls)

    if rating.has_toilet_paper is True:
        score += 5

    if rating.has_handicap_stall is True:
        score += 5

    if rating.has_seat_cover is True:
        score += 5

    if rating.has_baby_station is True:
        score += 5

    if rating.is_gender_neutral is True:
        score += 5

    if rating.has_hook is True:
        score += 5


    # Add all the raitings in the DB
    for toilet_rating in ratings:
        rating_count += 1
        score += int(toilet_rating.cleanliness)
        score += int(toilet_rating.cleanliness)
        score += int(toilet_rating.smell_rating)
        score += int(toilet_rating.artwork)
        score += int(toilet_rating.toilet_paper_quality)
        score += int(toilet_rating.flush_pressure)
        score -= int(toilet_rating.number_of_stalls)

        if toilet_rating.has_toilet_paper is True:
            score += 5

        if toilet_rating.has_handicap_stall is True:
            score += 5

        if toilet_rating.has_seat_cover is True:
            score += 5

        if toilet_rating.has_baby_station is True:
            score += 5

        if toilet_rating.is_gender_neutral is True:
            score += 5

        if toilet_rating.has_hook is True:
            score += 5

    score = (score / magic_number) % 5
    toilet.overall_rating = score
    toilet.rating_count = rating_count
    print("Overall rating for toilet: ", toilet_id, " = ", score)
    db_session.commit()

