from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
import logging

dbs = Blueprint('models', __name__)

logger = logging.getLogger(__name__)

