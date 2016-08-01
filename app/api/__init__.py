from flask import Blueprint
from flask_restful import Api

from app.api.resources.action import Action
from app.api.resources.host import HostCPUControl
from app.api.resources.scenario import Scenario
from app.api.resources.deployment import Deployment

import logging

logger = logging.getLogger(__name__)

api = Blueprint('api', __name__)

routes = Api(api)

routes.add_resource(Action, '/action')
routes.add_resource(HostCPUControl, '/cpu')
routes.add_resource(Scenario, '/scenario/<scenario_id>')
routes.add_resource(Deployment, '/deployment/<stack_id>/<application_id>')
