#!/usr/bin/env python
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

import logging
import requests


logger = logging.getLogger(__name__)


class ControllerAPI(object):

    def __init__(self, api_host='127.0.0.1', port=5000, user=None, password=None):
        self._api_host = api_host
        self._user = user
        self._password = password
        self._port = port

    def host_stress_cpu(self, host):
        url = "http://{0}:{1}/host/cpu?hostname={2}".format(self._api_host, self._port, host)
        logger.info(url)
        r = requests.post(url=url)

    def host_stress_disk(self):
        pass