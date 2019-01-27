from flask import (
    Blueprint, request, redirect, url_for, current_app, Response, session, g
)
import json
from .database import db_session
from .models import Toilet, Rating, User
from .auth import login_required
from .helper import *

bp = Blueprint('data', __name__, url_prefix='/data')


@bp.route('/contribute', methods=['POST'])
def contribute():
    session['t'] = request.form.get('toilet-form', '')

    if g.user is None:
        return redirect(url_for('auth.login'))

    update_toilet(session.get('t'))
    return redirect(url_for('index'))



@bp.route('/addtoilet', methods=['POST'])
def update_toilet():
    # print(flag)
    response = request.get_json()

    print(response)

    # Validate json data
    if response is None:
        return "Invalid JSON data"

    toilet = Toilet(response)

    # Update db
    db_session.add(toilet)
    db_session.commit()
    return str(toilet.id)

@bp.route('/addrating/<toilet_id>', methods=['POST'])
#@login_required
def update_rating(toilet_id):
    response = request.get_json()
    print(response)

    # Validate json data
    if response is None or id is None:
        return "Invalid JSON data"

    #user_id = session.get('user_id')
    user_id = 1 # TODO: Remove me
    rating = Rating(user_id, toilet_id, response)
    update_toilet_rank(toilet_id, rating)

    # Check db for existing rating
    existing_rating = db_session.query(User, Rating).filter(User.id == Rating.user_id and Rating.toilet_id == toilet_id).first()

    # if this user has rated this toilet, update their rating
    if existing_rating is not None:
        existing_rating.Rating.cleanliness = rating.cleanliness
        existing_rating.Rating.smell_rating = rating.smell_rating
        existing_rating.Rating.number_of_stalls = rating.number_of_stalls
        existing_rating.Rating.artwork = rating.artwork
        existing_rating.Rating.toilet_paper_quality = rating.toilet_paper_quality
        existing_rating.Rating.flush_pressure = rating.flush_pressure
        existing_rating.Rating.has_toilet_paper = rating.has_toilet_paper
        existing_rating.Rating.has_handicap_stall = rating.has_handicap_stall
        existing_rating.Rating.has_seat_cover = rating.has_seat_cover
        existing_rating.Rating.has_baby_station = rating.has_baby_station
        existing_rating.Rating.is_gender_neutral = rating.is_gender_neutral
        existing_rating.Rating.has_hook = rating.has_hook
        db_session.commit()
        return "\nUpdated"

    # Update user rating count
    user = db_session.query(User).filter(User.id == user_id).first()

    ## This should never be true, but safety
    if user is not None:
        user.rating_count += 1
        db_session.commit()

    # Update db
    db_session.add(rating)
    db_session.commit()
    print('Record was added successfully')

    return "\nok"


@bp.route('/toilets', methods=['GET'])
def get_toilets():
    res = db_session.query(Toilet).all()
    return Response(json.dumps([{
        'toilet_id'         :   x.id,
        'title'             :   x.title,
        'description'       :   x.description,
        'longitude'         :   x.longitude,
        'latitude'          :   x.latitude,
        'overall_rating'    :   x.overall_rating,
}
        for x in res]),
        mimetype='application/json')

@bp.route('/toilet/<toilet_id>', methods=['GET'])
def get_ratings(toilet_id):
    return Response(json.dumps([{
        'cleanliness'       :   x.cleanliness,
        'smell_rating'      :   x.smell_rating,
        'number_of_stalls'  :   x.number_of_stalls,
        'artwork'           :   x.artwork,
        'toilet_paper_quality' : x.toilet_paper_quality,
        'flush_pressure'    :   x.flush_pressure,
        'has_toilet_paper'  :   x.has_toilet_paper,
        'has_handicap_stall' :  x.has_handicap_stall,
        'has_seat_cover'    :   x.has_seat_cover,
        'has_baby_station'  :   x.has_baby_station,
        'has_hook'          :   x.has_hook,
        'is_gender_neutral' :   x.is_gender_neutral}
        for x in db_session.query(Rating).filter(Rating.toilet_id == toilet_id).all()]),
        mimetype='application/json')

