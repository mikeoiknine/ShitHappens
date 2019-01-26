from flask import (
    Blueprint, request, redirect, url_for, current_app, Response
)
import json
from .database import db_session

bp = Blueprint('data', __name__, url_prefix='/data')

@bp.route('/update', methods=['POST'])
def update_data():
    response = request.get_json()

    print(response)

    # Validate json data
    if response is None:
        return "Invalid JSON data"

    # Update db
    #db_session.add(sensor)
    #db_session.commit()
    #print('Record was added successfully')

    return str(response) + "\n"

@bp.route('/toilets', methods=['GET'])
def get_sensor_data():
    return Response(json.dumps([{
        #'temperature'       : query.temperature,
        #'pressure'          : query.pressure,
        #'humidity'          : query.humidity,
        #'gas_resistance'    : query.gas_resistance,
        'longitude'         : query.longitude,
        'latitude'          : query.latitude,
        #'timestamp'         : query.timestamp
        }
        for query in Sensor.query.all()]), mimetype='application/json')

