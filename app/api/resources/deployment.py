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
import os
from flask import request, make_response
from flask_restful import Resource
from fabric.api import run, execute, env, local
import app.models
import logging
import time

logger = logging.getLogger(__name__)


class Deployment(Resource):

    def get(self):
        """
        Handles GET request to sleep
        :return: response
        """

        if 'interval' in request.args:
            interval = float(request.args['interval'])
        else:
            interval = 0.0
        sleep_time = interval/1000.0
        logger.debug("Sleeping: {0} milli-seconds".format(int(interval)))
        time.sleep(sleep_time)

        return make_response('<h1>interval: {0}</h1>'.format(interval))
