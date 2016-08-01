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

from fabric.api import run, execute, task, env
import logging
import os

logger = logging.getLogger(__name__)


def run_command(command):
    """
    Run the input command on the server
    :return: None
    """
    logger.debug(command)
    run(command)

@task
def execute_command(host, command):
    """
    Fabric tasks to increase the load on a server
    :param host: Name of the host to stress the CPU
    :return: None
    """
    host_list = [host]
    env.use_ssh_config = True
    ssh_config_dir = '/etc/pulse-demo-control'
    if os.path.isdir(ssh_config_dir):
        env.ssh_config_path = os.path.join(ssh_config_dir, 'ssh_config')
        logger.info("Reading SSH configuration from: {0}".format(env.ssh_config_path))

    execute(run_command, command, hosts=host_list)

