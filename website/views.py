from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask_login import login_required, current_user
from .models import User, HouseKeeper, Booking
from . import db

views = Blueprint('views', __name__)

@views.route("/")
def front_page():
    return render_template("index.html", user=current_user)

@views.route("/contact")
def contact():
    return render_template("contact.html", user=current_user)

@views.route("/home")
@login_required
def home():
    return render_template("index.html", user=current_user)

@views.route("/index")
def index():
    return redirect(url_for("views.home"))

@views.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@views.route("/book")
@login_required
def book():
    return render_template("book.html", user=current_user)

@views.route("/account_type")
@login_required
def account_type():
    return render_template("account_type.html", user=current_user)


@views.route("/housekeeper_info", methods=['GET', 'POST'])
@login_required
def set_housekeeper():
    if request.method == 'POST':
        skillset = request.form.get("skillset")
        intro = request.form.get("intro")
        new_housekeeper = HouseKeeper(user_id=current_user.id, skillset=skillset, intro=intro)
        db.session.add(new_housekeeper)
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template("housekeeper.html", user=current_user)


@views.route('/api/househelps', methods=['GET'])
def get_househelps():
    househelps = HouseKeeper.query.all()
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
    new_househelp = HouseKeeper(
        name=data['name'],
        age=data['age'],
        services=data['services'],
        rating=data['rating']
    )
    db.session.add(new_househelp)
    db.session.commit()
    return jsonify({'message': 'HouseHelp registration successful!', 'househelp_id': new_househelp.id})

