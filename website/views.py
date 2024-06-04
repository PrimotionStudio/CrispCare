from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User, HouseKeeper, Booking
from . import db

views = Blueprint('views', __name__)


def get_user(user_id):
    return User.query.filter_by(id=user_id).first()
def get_booking(book_id):
    return Booking.query.filter_by(id=book_id).first()
def get_hk(hk_id):
    return HouseKeeper.query.filter_by(id=hk_id).first()

def get_housekeepers():
    housekeepers = HouseKeeper.query.all()
    users = []
    for housekeeper in housekeepers:
        users.append(User.query.filter_by(id=housekeeper.user_id).first())
    return list(enumerate(zip(users, housekeepers), 1))
    # Passing No argumnets return a list of tuples contaianing both users and houskeepers


@views.route("/")
def front_page():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    return render_template("index.html", user=current_user, hks=get_housekeepers())


@views.route("/contact")
def contact():
    return render_template("contact.html", user=current_user)


@views.route("/home")
@login_required
def home():
    return render_template("index.html", user=current_user, hks=get_housekeepers())


@views.route("/index")
def index():
    return redirect(url_for("views.home"))

# For housekeepers


@views.route("/profile/<hk_id>")
def profile_by_id(hk_id):
    housekeeper = HouseKeeper.query.filter_by(user_id=hk_id).first()
    if housekeeper:
        user = User.query.filter_by(id=housekeeper.user_id).first()
        return render_template("profile.html", user=current_user, hk=(user, housekeeper))
        # Passing an argumnets returns a tuples contaianing both users and houskeepers
    else:
        flash("Cannot access this profile", category="error")
        return redirect(url_for("views.home"))

# For ordinary users


@views.route("/profile")
@login_required
def profile():
    hk = HouseKeeper.query.filter_by(user_id=current_user.id).first()
    if hk:
        # Check first if the user is a registered housekeeper
        return redirect(url_for("views.profile_by_id", hk_id=current_user.id))
    return render_template("profile.html", user=current_user, hk=None)

# For ordinary users


@views.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    return render_template("settings.html", user=current_user)


@views.route("/bookings/accept", methods=["POST"])
@login_required
def accept_booking():
    if request.method == "POST":
        hk_id = request.form.get("hk_id")
        booking_id = request.form.get("book_id")
        if current_user.id == get_hk(hk_id).user_id:
            book = Booking.query.get(booking_id)
            book.status = "accepted"
            db.session.commit()
            flash("You have accepted this job", category="success")
        else:
            flash("An error occured while accepting booking", category="error")
    return redirect(url_for("views.bookings"))

@views.route("/bookings/decline", methods=["POST"])
@login_required
def decline_booking():
    if request.method == "POST":
        hk_id = request.form.get("hk_id")
        booking_id = request.form.get("book_id")
        if current_user.id == get_hk(hk_id).user_id:
            book = Booking.query.get(booking_id)
            book.status = "declined"
            db.session.commit()
            flash("You have declined this job", category="success")
        else:
            flash("An error occured while declining booking", category="error")
    return redirect(url_for("views.bookings"))


@views.route("/bookings/terminate", methods=["POST"])
@login_required
def terminate_booking():
    if request.method == "POST":
        hk_id = request.form.get("hk_id")
        booking_id = request.form.get("book_id")
        if current_user.id == get_hk(hk_id).user_id or current_user.id == get_booking(booking_id).user_id:
            book = Booking.query.get(booking_id)
            book.status = "terminated"
            db.session.commit()
            flash("You have terminated this job", category="success")
        else:
            flash("An error occured while terminating booking", category="error")
    return redirect(url_for("views.bookings"))


@views.route("/bookings/complete", methods=["POST"])
@login_required
def complete_booking():
    if request.method == "POST":
        hk_id = request.form.get("hk_id")
        booking_id = request.form.get("book_id")
        if current_user.id == get_hk(hk_id).user_id or current_user.id == get_booking(booking_id).user_id:
            book = Booking.query.get(booking_id)
            book.status = "completed"
            db.session.commit()
            flash("You have marked this job as completed", category="success")
        else:
            flash("An error occured while completing job", category="error")
    return redirect(url_for("views.bookings"))


@views.route("/bookings")
@login_required
def bookings():
    if current_user.role == "housekeeper":
        hk = HouseKeeper.query.filter_by(user_id=current_user.id).first()
        bookings = Booking.query.filter_by(housekeeper_id=hk.id).all()
        clients = []
        for booking in bookings:
            clients.append(get_user(booking.user_id))
        return render_template("bookings.html", user=current_user, bookings=zip(bookings, clients))
    else:
        bookings = Booking.query.filter_by(user_id=current_user.id).all()
        hks = []
        for booking in bookings:
            hks.append(get_user(get_hk(booking.housekeeper_id).user_id))
        return render_template("bookings.html", user=current_user, bookings=zip(bookings, hks))


@views.route("/book/<hk_id>", methods=["GET", "POST"])
@login_required
def book(hk_id):
    if request.method == "POST":
        description = request.form.get("description")
        location = request.form.get("location")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        new_booking = Booking(user_id=current_user.id, housekeeper_id=hk_id,
                              description=description, start_date=start_date, end_date=end_date, location=location)
        db.session.add(new_booking)
        db.session.commit()
        flash(f"You have booked {get_user(get_hk(hk_id).user_id).fullname} for {
              start_date}", category="success")
        return redirect(url_for("views.profile_by_id", hk_id=hk_id))
    else:
        housekeeper = HouseKeeper.query.filter_by(user_id=hk_id).first()
        if hk_id == current_user.id or not housekeeper:
            flash("Cannot access this profile", category="error")
            return redirect(url_for("views.home"))
        else:
            user = User.query.filter_by(id=housekeeper.user_id).first()
            return render_template("book.html", user=current_user, hk=(user, housekeeper))
            # Passing an argumnets returns a tuples contaianing both users and houskeepers


@views.route("/account_type")
@login_required
def account_type():
    return render_template("account_type.html", user=current_user)


@views.route("/housekeeper_info", methods=['GET', 'POST'])
@login_required
def set_housekeeper():
    if request.method == 'POST':
        skillset = request.form.get("skillset").strip()
        intro = request.form.get("intro").strip()
        old_housekeeper = HouseKeeper.query.filter_by(
            user_id=current_user.id).first()
        if old_housekeeper:
            # Then update the housekeeper's info
            old_housekeeper.skillset = skillset
            old_housekeeper.intro = intro
        else:
            # else create new housekeeper's info
            new_housekeeper = HouseKeeper(
                user_id=current_user.id, skillset=skillset, intro=intro)
            db.session.add(new_housekeeper)
            current_user.role = "housekeeper"
        db.session.commit()
        flash("Information updated successfully", category="success")
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
