from flask import Blueprint
from flask_restful import Api

from application.api.resources.host import HostCPUControl
from application.api.resources.scenario import Scenario
from application.api.resources.deployment import Deployment

import logging

logger = logging.getLogger(__name__)

apis = Blueprint('api', __name__)
api = Api(apis)

api.add_resource(HostCPUControl, '/cpu')

logger.debug("Add resource Scenario to path: /scenario/<scenario_id")
api.add_resource(Scenario, '/scenario/<scenario_id>')

logger.debug("Add resource Deployment to path: /deployment/<stack_id>/<application_id>")
api.add_resource(Deployment, '/deployment/<stack_id>/<application_id>')
