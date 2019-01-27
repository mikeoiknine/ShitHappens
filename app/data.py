from flask import (
    Blueprint, request, redirect, url_for, current_app, Response, session, g
)
import json
from .database import db_session
from .models import Toilet, Rating
from .auth import login_required

bp = Blueprint('data', __name__, url_prefix='/data')


@bp.route('/contribute', methods=['POST'])
def contribute():
    session['t'] = request.form.get('toilet-form', '')

    if g.user is None:
        return redirect(url_for('auth.login'))

    update_toilet(session.get('t'))
    return redirect(url_for('index'))



def update_toilet(flag):
    print(flag)
    # response = request.get_json()

    #print(response)

    ## Validate json data
    #if response is None:
    #    return "Invalid JSON data"

    #toilet = Toilet(response)

    ## Update db
    #db_session.add(toilet)
    #db_session.commit()
    #print('Record was added successfully')
    return "ok"
    #return str(toilet.id)

@bp.route('/addrating/<id>', methods=['POST'])
@login_required
def update_rating(id):
    response = request.get_json()

    print(response)

    # Validate json data
    if response is None or id is None:
        return "Invalid JSON data"

    rating = Rating(id, response)

    # Update db
    db_session.add(rating)
    db_session.commit()
    print('Record was added successfully')

    return "\nok"

@bp.route('/toilets', methods=['GET'])
def get_toilets():
    res2 = db_session.query(Rating, Toilet).filter(Toilet.id == Rating.toilet_id).all()
    return Response(json.dumps([{
        'toilet_id':   x.Toilet.id,
        'longitude':   x.Toilet.longitude,
        'latitude' :   x.Toilet.latitude,
        'Rating'   :   x.Toilet.overall_rating,
        'rated by' :   x.Rating.id}
        for x in res2]),
        mimetype='application/json')
