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

from scenario import Scenario
from action import Action
from application.api.control.deploy_app import set_application_revision


class PushBasePage(Action):

    def __init__(self, i):
        super(PushBasePage, self).__init__(i)
        self.stack_id = None
        self.application_id = None
        self.revision = None
        self.hosts = None

    def run(self):

class PushGoodPage(PushBasePage):

    def __init__(self, i):
        super(PushBasePage, self).__init__(i)


class PushBadPage(PushBasePage):

    def __init__(self, i):
        super(PushBadPage, self).__init__(i)


class FBNDevOps(Scenario):

    def __init__(self, i):
        super(FBNDevOps, self).__init__(i)

        self._actions[1] = PushBadPage(1, "web-1")

    def execute(self, action_id):
        action = self._actions[int(action_id)]
        action.run()
