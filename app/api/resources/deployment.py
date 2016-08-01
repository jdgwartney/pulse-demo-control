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
from string import replace
import logging
from app.api.control.deploy_app import set_application_revision, deploy_application

logger = logging.getLogger(__name__)


class Deployment(Resource):

    def __init__(self):
        pass

    def post(self, stack_id, application_id):
        """
        Handles POST request on a scenario resource
        :param application_id: Opswork application ID
        :return: response
        """
        revision = request.args['revision']
        hosts = request.args['hosts']
        hosts = replace(hosts, ',', ' ')

        # Set the revision on the application
        # set_application_revision(application_id, revision)

        # Deploy the application to the selected hosts
        # deploy_application(stack_id, application_id, hosts)

        return make_response("<h1>{0} {1}, args: {2} {3}</h1>".format(
            request.method, request.path, stack_id, application_id, revision, hosts))

