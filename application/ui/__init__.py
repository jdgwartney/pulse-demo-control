from flask import Blueprint, render_template
import logging

logger = logging.getLogger(__name__)

uis = Blueprint('ui', __name__, template_folder='templates', static_folder='static')


@uis.route('/')
def index():
    logger.debug("index()")
    return render_template("index.html")


@uis.route('/login')
def login():
    logger.debug("index()")
    return render_template("login.html")


@uis.route('/scenarios')
def scenarios():
    logger.debug("scenarios()")
    return render_template("scenarios.html")


@uis.route('/control')
def control():
    logger.debug("control()")
    return render_template("control.html")







