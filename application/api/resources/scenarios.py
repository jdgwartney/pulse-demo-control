from flask import request, make_response
from flask_restful import Resource


class HostCPUControl(Resource):

    def __init__(self):
       pass

    def post(self):
        """Handling of POST requests."""
	return make_response("<h1>POST {0}, args: {1}</h1>".format(request.method, request.args.get('host','')))

    def get(self):
        """Handling of GET requests."""
        return "GET {0}</h1>".format(request.method)
