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

from fabric.api import run, execute, task, env
import logging
import os

logger = logging.getLogger(__name__)


def stress_cpu(timeout):
    """
    Run the stress program to load the CPU on the server
    :return: None
    """
    command = "stress --cpu 8 --io 4 --vm 2 --vm-bytes 128M --timeout {0}s".format(timeout)
    logger.debug(command)
    run(command)

@task
def cpu_load(host, timeout=60):
    """
    Fabric tasks to increase the load on a server
    :param host: Name of the host to stress the CPU
    :return: None
    """
    # This is the magic you don't get with @hosts or @roles.
    # Even lazy-loading roles require you to declare available roles
    # beforehand. Here, the sky is the limit.
    host_list = [host]
    env.use_ssh_config = True
    ssh_config_dir = '/etc/pulse-demo-control'
    if os.path.isdir(ssh_config_dir):
        env.ssh_config_path = os.path.join(ssh_config_dir, 'ssh_config')
        logger.info("Reading SSH configuration from: {0}".format(env.ssh_config_path))

    # Put this dynamically generated host list together with the work to be
    # done.
    execute(stress_cpu, timeout, hosts=host_list)


if __name__ == "__main__":
    cpu_load("mon-1.flybynightfares.com")
