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


def cpu_load():
    run('stress --cpu 8 --io 4 --vm 2 --vm-bytes 128M --timeout 60s')

# This is the user-facing task invoked on the command line.
@task
def deploy(host):
    # This is the magic you don't get with @hosts or @roles.
    # Even lazy-loading roles require you to declare available roles
    # beforehand. Here, the sky is the limit.
    host_list = [host]
    env.use_ssh_config = True

    # Put this dynamically generated host list together with the work to be
    # done.
    execute(cpu_load, hosts=host_list)


if __name__ == "__main__":
    deploy("mon-1.flybynightfares.com")
