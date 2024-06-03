from flask import Blueprint, request, jsonify
from app.models.review import Review

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/househelps/<int:househelp_id>/reviews', methods=['POST'])
def create_review(househelp_id):
    data = request.get_json()
    # Create a new review based on the data
    new_review = Review(househelp_id=househelp_id, ...)
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201

