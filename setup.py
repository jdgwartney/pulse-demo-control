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
from distutils.core import setup

setup(
    name='tsctl',
    version='0.1.0',
    url='https://ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/pulse-demo-control',
    author='David Gwartney',
    author_email='david_gwartney@bmc.com',
    packages=['tsctl', ],
    package_data={'tsctl': ['templates/*.html']},
    license='Apache 2',
    description='Python Bindings for the TrueSight Pulse REST APIs',
    long_description=open('README.txt').read(),
    entry_points={
        'console_scripts': [
            'ts-control = tsctl.cli:main',
            'ts-controld = tsctl.server:main',
        ]
    },
    install_requires=[
        "requests >= 2.3.0",
    ],
)
