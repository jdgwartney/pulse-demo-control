from flask import Blueprint
from flask_restful import Api

from application.api.resources.host import HostCPUControl
from application.api.resources.scenario import Scenario

apis = Blueprint('api', __name__)
api = Api(apis)


api.add_resource(HostCPUControl, '/cpu')
api.add_resource(Scenario, '/scenario/<scenario_id>')
