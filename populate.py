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

db.drop_all()
db.create_all()


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
            "{args} --stack-id {stack_id} --app-id {app_id} --command '{command}' --instance-ids {instance_ids}".format(
                args='opsworks create-deployment',
                stack_id=stack_id,
                app_id=app_id,
                command='{"Name":"deploy"}',
                instance_ids=ids
            ))


#
# CPU Load
#
cpu_load_name = "cpu_load"
scenario_cpu_load = Scenario(name=cpu_load_name)
add_and_commit([scenario_cpu_load])

action = Action(name='load_host', scenario_id=scenario_cpu_load.id)
add_and_commit([action])

cmd = 'stress'
args = '-cpu 8 --io 4 --vm 2 --vm-bytes 128M --timeout 60s'
command = Command(name='load_cpu', cmd=cmd, args=args, host='web-1', order=1, action_id=action.id)

add_and_commit([command])

#
# DevOps
#

devops_name = 'devops'
devops_title = 'Fly By Night Fares - DevOps In Action'
devops_page = 'ui.scenario_devops'
scenario_devops = Scenario(name=devops_name, title=devops_title, page=devops_page)

add_and_commit([scenario_devops])

# Define actions associated with the scenario

STACK_ID = 'e9c7a15b-180a-42bb-becb-40fed055f4bc'
APPLICATION_ID = 'ae0a0232-a545-4250-99a3-5243d9b2c570'

BASE_APP_BRANCH = 'version-1'
BAD_APP_BRANCH = 'version-2'
IMPROVED_APP_BRANCH = 'version-3'

WEB_TEST_INSTANCES = [
    '4f9685d9-43f9-4926-81be-4b815f7086f2'
]

web_1 = '4f9685d9-43f9-4926-81be-4b815f7086f2',
web_2 = '36bacec9-63e1-4739-b63c-0720dd05ef01',
web_3 = '0e8577f3-dde4-4ec0-b020-35c62f6d2652',
web_4 = '46932149-a21d-4570-869e-954baf3a46e9',
web_5 = '4c9e4705-d793-4c6e-8a20-d53cc7e5dcdf'

WEB_INSTANCES = [
    '4f9685d9-43f9-4926-81be-4b815f7086f2',
    '36bacec9-63e1-4739-b63c-0720dd05ef01',
    '0e8577f3-dde4-4ec0-b020-35c62f6d2652',
    '46932149-a21d-4570-869e-954baf3a46e9',
    '4c9e4705-d793-4c6e-8a20-d53cc7e5dcdf'
]

AWS_HOST = None

action_1 = Action(name='reset', scenario_id=scenario_devops.id)
action_2 = Action(name='bad_page_to_host', scenario_id=scenario_devops.id)
action_3 = Action(name='revert_bad_page_to_host', scenario_id=scenario_devops.id)
action_4 = Action(name='improved_page_to_host', scenario_id=scenario_devops.id)
action_5 = Action(name='improved_page_to_all_hosts', scenario_id=scenario_devops.id)

add_and_commit([action_1, action_2, action_3, action_4, action_5])

# Reset
(cmd, args) = aws_opsworks_update_app(app_id=APPLICATION_ID, revision=BASE_APP_BRANCH)
command_1 = Command(name='set base revision', cmd=cmd, args=args, order=1, action_id=action_1.id)

(cmd, args) = aws_opsworks_create_deployment(stack_id=STACK_ID, app_id=APPLICATION_ID, instance_ids=WEB_INSTANCES)
command_2 = Command(name='deploy base revision', cmd=cmd, args=args, order=2, action_id=action_1.id)

add_and_commit([command_1, command_2])

# Step 1 - Deploy Change to a Single Node

(cmd, args) = aws_opsworks_update_app(app_id=APPLICATION_ID, revision=BAD_APP_BRANCH)
command_1_1 = Command(name='set bad revision', cmd=cmd, args=args, order=1, host=AWS_HOST, action_id=action_2.id)

(cmd, args) = aws_opsworks_create_deployment(stack_id=STACK_ID, app_id=APPLICATION_ID, instance_ids=WEB_TEST_INSTANCES)
command_1_2 = Command(name='deploy bad revision', cmd=cmd, args=args, order=2, host=AWS_HOST, action_id=action_2.id)

add_and_commit([command_1_1, command_1_2])

# Step-2 Revert Code Change

(cmd, args) = aws_opsworks_update_app(app_id=APPLICATION_ID, revision=BASE_APP_BRANCH)
command_2_1 = Command(name='set base revision', cmd=cmd, args=args, order=1, host=AWS_HOST, action_id=action_3.id)

(cmd, args) = aws_opsworks_create_deployment(stack_id=STACK_ID, app_id=APPLICATION_ID,
                                             instance_ids=WEB_TEST_INSTANCES)
command_2_2 = Command(name='deploy base revision', cmd=cmd, args=args, order=2, host=AWS_HOST, action_id=action_3.id)

add_and_commit([command_2_1, command_2_2])

# Step 4 - Deploy Revised Code Change

(cmd, args) = aws_opsworks_update_app(app_id=APPLICATION_ID, revision=IMPROVED_APP_BRANCH)
command_4_1 = Command(name='set improved revision', cmd=cmd, args=args, order=1, host=AWS_HOST, action_id=action_4.id)

(cmd, args) = aws_opsworks_create_deployment(stack_id=STACK_ID, app_id=APPLICATION_ID, instance_ids=WEB_TEST_INSTANCES)
command_4_2 = Command(name='deploy improved revision', cmd=cmd, args=args, order=2, host=AWS_HOST, action_id=action_4.id)

add_and_commit([command_4_1, command_4_2])

# Step 5 - Deploy to Code Change to All Nodes

(cmd, args) = aws_opsworks_create_deployment(stack_id=STACK_ID, app_id=APPLICATION_ID,
                                             instance_ids=WEB_INSTANCES)
command_5_1 = Command(name='deploy to all hosts', cmd=cmd, args=args, order=1, host=AWS_HOST, action_id=action_5.id)

add_and_commit([command_5_1])
