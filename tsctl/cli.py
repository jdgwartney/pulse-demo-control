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


class ControlCLI(object):

    def __init__(self):
        self._command_map = {}
        self._command_map['cpu-load'] = self._stress_host

    def _stress_host(self):
        host = self._args.host
        url = "http://127.0.0.1:5000/host/cpu?hostname={0}".format(host)
        print(url)
        r = requests.post(url=url)

    def _arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--user', action='store', help='User to authenticate with')
        subparsers = parser.add_subparsers(help='Performance commands', dest="command")

        create_parser = subparsers.add_parser('cpu-load', help='Stress the CPU on a host')
        create_parser.add_argument('--host', action='store', dest='host', required=True, help='Name of the host to stress the CPU')

        create_parser = subparsers.add_parser('disk-space', help='Fill up the disk on a host')
        create_parser.add_argument('--host', action='store', help='Name of the host to fill up the disk space')

        create_parser = subparsers.add_parser('disk-load', help='Load up the disk on a host')
        create_parser.add_argument('--host', action='store', help='Name of the host to load up the disk')

        create_parser = subparsers.add_parser('memory-load', help='Use memory on the host')
        create_parser.add_argument('--host', action='store', help='Name of the host to use memory')

        self._args = parser.parse_args()

    def _run(self):
        command = self._command_map[self._args.command]
        command()

    def execute(self):

        self._arguments()
        self._run()


def main():
    cli = ControlCLI()
    cli.execute()


if __name__ == "__main__":
    main()
