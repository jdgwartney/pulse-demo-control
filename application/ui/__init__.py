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


@uis.route('/scenarios/prototype')
def scenario_prototype():
    logger.debug("scenario_prototype()")
    return render_template("prototype.html")


@uis.route('/scenarios/devops')
def scenario_devops():
    logger.debug("scenario_devops()")
    return render_template("devops.html")


@uis.route('/scenarios/here')
def scenario_here():
    logger.debug("scenario_here()")
    return render_template("here.html")


@uis.route('/control')
def control():
    logger.debug("control()")
    return render_template("control.html")







