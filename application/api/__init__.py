from flask import Blueprint
from flask_restful import Api

apis = Blueprint('api', __name__)
api = Api(apis)

from application.api.resources.host import HostCPUControl

api.add_resource(HostCPUControl, '/cpu')
