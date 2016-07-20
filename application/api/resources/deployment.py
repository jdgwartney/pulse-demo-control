from flask import request, make_response
from flask_restful import Resource
from string import replace
import logging
from application.api.control.deploy_app import set_application_revision, deploy_application

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

