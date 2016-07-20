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

from fabric.api import run, execute, task, local
import logging

logger = logging.getLogger(__name__)


@task
def set_application_revision(application_id, revision):
    """
    Fabric task to change the application version
    :param host: Name of the host to stress the CPU
    :return: None
    """
    command = "aws opsworks update-app --app-id {0} --app-source Revision={1}".format(application_id, revision)
    logger.debug(command)
    local(command)


@task
def deploy_application(stack_id, application_id, hosts):
    """
    Deploy the application using OpsWorks
    :param stack_id: Id of the stack that contains the application to deploy
    :param application_id: Id of the application to deploy
    :param hosts: Host to deploy the application to
    :return:
    """
    command = 'aws opsworks create-deployment '
    command += '--stack-id {0} --app-id {1} --instance-ids {2} --command {"Name": "deploy"}'.format(
        stack_id, application_id, hosts)


