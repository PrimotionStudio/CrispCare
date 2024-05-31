from flask import Flask
from main_app.views import views

from flask_mysqldb import MySQL


def create_app():
    app = Flask(__name__)
    # app.config.from_object('config')
    # from main_app.main.views import main as main_blueprint
    app.register_blueprint(views)
    app.secret_key = 'its a secret'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'crisp_care'

	mysql = MySQL(app)
    return app
