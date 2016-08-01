#
# Copyright 2016 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from flask import request, make_response
from flask_restful import Resource
import app.models
import logging

logger = logging.getLogger(__name__)


class Action(Resource):

    def __init__(self):
        self.action = None
        self.scenario = None
        self.commands = None
        self.host = None

    def execute(self):
        pass

    def lookup(self):
        scenario = app.models.Scenario.query.filter_by(name=self.scenario).first()
        logger.debug("found scenario: name='{0}', id={1}".format(scenario.name, scenario.id))
        action = app.models.Action.query.filter_by(scenario_id=scenario.id).first()
        logger.debug("found action: name='{0}', id={1}".format(action.name, action.id))

        for command in action.commands:
            logger.info(command)

    def post(self):
        """
        Handles POST request on a scenario resource
        :return: response
        """

        self.scenario = request.args['scenario']
        self.action = request.args['action']
        logger.debug("Running action: {0}, from scenario: {1}".format(self.scenario, self.action))

        self.lookup()

        return make_response("<h1>{0} {1}, args: {2} {3}</h1>".format(
            request.method,
            request.path,
            self.scenario,
            self.action))
