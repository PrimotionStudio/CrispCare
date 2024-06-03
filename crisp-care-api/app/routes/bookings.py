from flask import Blueprint, request, jsonify
from app.models.booking import Booking

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/', methods=['POST'])
def create_booking():
    data = request.get_json()
    # Create a new booking based on the data
    new_booking = Booking(...)
    db.session.add(new_booking)
    db.session.commit()
    return jsonify(new_booking.to_dict()), 201

@bookings_bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manage_booking(id):
    booking = Booking.query.get(id)
    if request.method == 'GET':
        return jsonify(booking.to_dict())
    elif request.method == 'PUT':
        # Update the booking details
        db.session.commit()
        return jsonify(booking.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(booking)
        db.session.commit()
        return jsonify({'message': 'Booking deleted'}), 204

