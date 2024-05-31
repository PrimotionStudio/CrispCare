from . import db
from flask_login import UserMixin

class HouseHelp(db.Model):
    __tablename__ = 'househelps'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    services = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=True)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    househelp_id = db.Column(db.Integer, db.ForeignKey('househelps.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    requirements = db.Column(db.String(200), nullable=True)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Flask-Login properties
    @property
    def is_active(self):
        return True

    def get_id(self):
        return self.id

