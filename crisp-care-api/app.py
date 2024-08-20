from flask import Flask
from app.routes.auth import auth_bp
from app.routes.househelps import househelps_bp
from app.routes.bookings import bookings_bp
from app.routes.reviews import reviews_bp
from app.routes.users import users_bp
from app import db

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(househelps_bp, url_prefix='/api/househelps')
app.register_blueprint(bookings_bp, url_prefix='/api/bookings')
app.register_blueprint(reviews_bp, url_prefix='/api/reviews')
app.register_blueprint(users_bp, url_prefix='/api/users')

if __name__ == '__main__':
    app.run()

