# main/routes.py
from flask import render_template, request, Blueprint
from acrevest.models import Property

from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    properties = Property.query.order_by(Property.date_listed.desc()).paginate(page=page, per_page=10)
    return render_template('home.html', properties=properties)

@main.route("/about")
def about():
    return render_template('about.html', title='About')
