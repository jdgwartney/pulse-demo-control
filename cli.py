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

import argparse
import requests
from cpu import HostCpuControl


class ControlCLI(object):

    def __init__(self):
        self._command_map = {}
        self._command_map['cpu-load'] = self._stress_host
        self._commands = []

        self._commands.append(HostCpuControl())



    def _arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--user', action='store', help='User to authenticate with')
        sub_parser = parser.add_subparsers(help='Performance commands', dest="command")

        create_parser = sub_parser.add_parser('disk-space', help='Fill up the disk on a host')
        create_parser.add_argument('--host', action='store', help='Name of the host to fill up the disk space')

        create_parser = sub_parser.add_parser('disk-load', help='Load up the disk on a host')
        create_parser.add_argument('--host', action='store', help='Name of the host to load up the disk')

        create_parser = sub_parser.add_parser('memory-load', help='Use memory on the host')
        create_parser.add_argument('--host', action='store', help='Name of the host to use memory')

        for command in self._commands:
            command.add_parser(sub_parser)

        self._args = parser.parse_args()

    def _run(self):
        command = self._commands[self._args.command]
        command.handle_arguments(command)

    def execute(self):

        self._arguments()
        self._run()


def main():
    cli = ControlCLI()
    cli.execute()


if __name__ == "__main__":
    main()
