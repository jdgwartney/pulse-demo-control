from flask import request, make_response
from flask_restful import Resource
import logging

from app.api.scenarios import CPULoadOnWebServer

logger = logging.getLogger(__name__)


class Scenario(Resource):
    def __init__(self):
        self._scenarios = {}
        self._scenarios[1] = CPULoadOnWebServer(1)

    def post(self, scenario_id=None):
        """
        Handles POST request on a scenario resource
        :param scenario_id: Unique scenario id
        :param action_id: Unique action id
        :return: response
        """

        scenario = self._scenarios[int(scenario_id)]
        action_id = request.args['action_id']
        logger.debug("Running action: {0}, from scenario: {1}".format(scenario_id, action_id))
        scenario.execute(action_id)

        return make_response("<h1>{0} {1}, args: {2}</h1>".format(request.method, request.path, action_id))

    def get(self, id):
        """Handling of GET requests."""
        return "GET {0}</h1>".format(request.method)
