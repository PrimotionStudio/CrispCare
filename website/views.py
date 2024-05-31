# website/views.py

from flask import Blueprint, request, jsonify
from flask_login import login_required
from .models import User, HouseHelp, Booking
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return "Welcome to CrispCare!"

@views.route('/api/househelps', methods=['GET'])
def get_househelps():
    househelps = HouseHelp.query.all()
    househelps_list = []
    for h in househelps:
        househelp_dict = {
            'id': h.id,
            'name': h.name,
            'age': h.age,
            'services': h.services,
            'rating': h.rating
        }
        househelps_list.append(househelp_dict)
    return jsonify(househelps_list)

@views.route('/api/book', methods=['POST'])
def book_househelp():
    data = request.get_json()
    new_booking = Booking(
        user_id=data['user_id'],
        househelp_id=data['househelp_id'],
        date=data['date'],
        time=data['time'],
        requirements=data.get('requirements', '')
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({'message': 'Booking successful!'})

@views.route('/api/register_househelp', methods=['POST'])
def register_househelp():
    data = request.get_json()
    new_househelp = HouseHelp(
        name=data['name'],
        age=data['age'],
        services=data['services'],
        rating=data['rating']
    )
    db.session.add(new_househelp)
    db.session.commit()
    return jsonify({'message': 'HouseHelp registration successful!', 'househelp_id': new_househelp.id})

