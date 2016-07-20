from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
import logging

dbs = Blueprint('db', __name__)


logger = logging.getLogger(__name__)
db = SQLAlchemy()

