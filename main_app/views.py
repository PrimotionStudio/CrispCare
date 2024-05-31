from flask import Blueprint, render_template, redirect, url_for

views = Blueprint("main_app_views", __name__)

@views.route("/")
def home():
    return render_template("index.html")


@views.route("/home")
def _home():
    return redirect(url_for("main_app_views.home"))


@views.route("/index")
def index():
    return redirect(url_for("main_app_views.home"))


@views.route("/contact")
def contact():
    return render_template("contact.html")


@views.route("/auth")
def auth():
    return render_template("signin_signup.html")
	

@views.route("/profile")
def profile():
    return render_template("profile.html")


@views.route("/book")
def book():
    return render_template("book.html")