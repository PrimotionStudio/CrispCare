from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    housekeeper_id = db.Column(db.Integer, db.ForeignKey('housekeeper.id'), nullable=False)
    description = db.Column(db.String(5000), nullable=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default='booked') # status: booked, pending, terminated, completed

class HouseKeeper(db.Model):
    __tablename__ = 'housekeeper'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skillset = db.Column(db.String(200), nullable=False)
    intro = db.Column(db.String(5000), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    bookings = db.relationship("Booking", backref='housekeeper', lazy=True)

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="homeowner") # roles: homeowner, housekeeper
    bookings = db.relationship('Booking', backref='user', lazy=True)
    

    # Flask-Login properties
    # @property
    # def is_active(self):
    #     return True

    # def get_id(self):
    #     return self.id

