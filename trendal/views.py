from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
def home():
    user = current_user
    return render_template("index.html", user=user)

