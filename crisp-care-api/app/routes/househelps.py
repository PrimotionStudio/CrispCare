from flask import Blueprint, request, jsonify
from app.models.househelp import HouseHelp
from sqlalchemy import and_

househelps_bp = Blueprint('househelps', __name__)

@househelps_bp.route('/search', methods=['POST'])
def search_house_helps():
    data = request.get_json()
    location = data.get('location')
    services = data.get('services')
    availability = data.get('availability')
    min_rating = data.get('min_rating', 0)

    query = HouseHelp.query

    if location:
        query = query.filter(HouseHelp.location.like(f'%{location}%'))
    if services:
        query = query.filter(HouseHelp.services.like(f'%{services}%'))
    if availability:
        # Implement the availability filter logic
        pass

    results = query.filter(HouseHelp.rating >= min_rating).all()
    return jsonify([househelp.to_dict() for househelp in results])



@househelps_bp.route('/<int:id>/availability/calendar', methods=['GET'])
def get_availability_calendar(id):
    househelp = HouseHelp.query.get(id)
    # Generate the availability calendar based on the househelp's availability data
    calendar = generate_availability_calendar(househelp.availability)
    return jsonify(calendar)


