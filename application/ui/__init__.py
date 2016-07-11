from flask import Blueprint, render_template

uis = Blueprint('ui', __name__, template_folder='templates', static_folder='static')


@uis.route('/')
def index():
    return render_template("index.html")


@uis.route('/login')
def login():
    return render_template("login.html")


@uis.route('/scenarios')
def scenarios():
    return render_template("scenarios.html")


@uis.route('/control')
def control():
    return render_template("control.html")







