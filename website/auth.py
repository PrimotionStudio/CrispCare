from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from .views import views

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form.get("fullname").strip()
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if fullname == "" or email == "" or password == "":
            flash("Please fill all fields", category="error")
        elif user:
            flash("This email is already registered", category="error")
        else:
            # All is good here
            password = generate_password_hash(request.form.get("password"), method="pbkdf2:md5")
            new_user = User(fullname=fullname, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created", category="success")
            return redirect(url_for('views.account_type'))
    return render_template("signin_signup.html", user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if email == "" or password == "":
            flash("Please fill all fields", category="error")
        elif not user:
            flash("This email is not linked to an account", category="error")
        else:
            # All is good here
            if user:
                if check_password_hash(user.password, password):
                    login_user(user, remember=True)
                    flash("Login Successful", category="success")
                    return redirect(url_for('views.home'))
                else:
                    flash("Incorrect password", category="error")
            else:
                flash("This email is not linked to an account", category="error")
    return render_template("signin_signup.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

