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

from control import ControlCLI


class HostCpuControl(ControlCLI):

    def __init__(self):
        super(HostCpuControl, self).__init__()

    @property
    def name(self):
        return 'cpu-load'

    @property
    def help(self):
        return 'Stress the CPU on a host'

    def add_parser(self, sub_parser):
        super(HostCpuControl, self).add_parser(sub_parser)

        self._parser.add_argument('--host', action='store', dest='host', metavar='host', required=True,
                                  help='Name of the host to stress the CPU')

    def handle_arguments(self, args):
        super(HostCpuControl, self).handle_arguments(args)

