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
from app import db
from app.models import Action, Command, Scenario
import logging

logger = logging.getLogger(__name__)


# db.drop_all()
# db.create_all()


def add_and_commit(items):
    for item in items:
        db.session.add(item)
    db.session.commit()


def aws_opsworks_update_app(app_id, revision):
    return ('aws', "opsworks update-app --app-id {app_id} --app-source Revision={revision}".format(
        app_id=app_id,
        revision=revision
    ))


def aws_opsworks_create_deployment(stack_id, app_id, instance_ids):
    ids = ' '.join(instance_ids)
    return ('aws',
            "{args} --stack-id {stack_id} --app-id {app_id} --command {command} --instance_ids {instance_ids}".format(
                args='opsworks create-deployment',
                stack_id=stack_id,
                app_id=app_id,
                command='{"Name":"deploy"}',
                instance_ids=ids
            ))


# Define our the name of our Scenario
scenario_name = 'DevOps'
scenario_devops = Scenario(name=scenario_name)

add_and_commit([scenario_devops])

# Define actions associated with the scenario

STACK_ID = 'e9c7a15b-180a-42bb-becb-40fed055f4bc'
APPLICATION_ID = 'ae0a0232-a545-4250-99a3-5243d9b2c570'

BASE_APP_REVISION = '1'
BAD_APP_REVISION = '2'

action_1 = Action(name='Reset Scenario', scenario_id=scenario_devops.id)
action_2 = Action(name='Push Bad Page To Single Host', scenario_id=scenario_devops.id)
action_3 = Action(name='Revert Bad Page To Single Host', scenario_id=scenario_devops.id)
action_4 = Action(name='Push Improved Page To Single Host', scenario_id=scenario_devops.id)
action_5 = Action(name='Push Improved Page To All Hosts', scenario_id=scenario_devops.id)

add_and_commit([action_1, action_2, action_3, action_4, action_5])

(cmd, args) = aws_opsworks_update_app(app_id=APPLICATION_ID,
                                      revision=BASE_APP_REVISION)

# Action 1 Commands
command_1 = Command(name='Set application to base revision',
                    cmd=cmd,
                    args=args,
                    order=1,
                    action_id=action_1.id)

(cmd, args) = aws_opsworks_create_deployment(stack_id=STACK_ID, app_id=APPLICATION_ID, instance_ids=['foo', 'bar'])
command_2 = Command(name='Deploy application base revision',
                    cmd=cmd,
                    args=args,
                    order=2,
                    action_id=action_1.id)

add_and_commit([command_1, command_2])

# Action 2 Commands



