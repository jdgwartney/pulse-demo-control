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


class ControlCLI(object):

    def __init__(self):
        self._parser = None

    @property
    def name(self):
        return None

    @property
    def help(self):
        return None

    def add_parser(self, parser):
        self._parser = parser.add_parser(self.name, help=self.help)
        self._parser.add_argument('-a', '--api-host', action='store', dest='api_host', metavar='api_host',
                                  required=False, help='Host name of the demo controller')
        self._parser.add_argument('-u', '--user', action='store', dest='user', metavar='user',
                                  required=False, help='User to authenticate to the demo controller')
        self._parser.add_argument('-p', '--password', action='store', dest='password', metavar='password',
                                  required=False, help='Password to authenticate to the demo controller')

    def handle_arguments(self, args):
        if args.api_host is not None:
            self._api_host = args.self

