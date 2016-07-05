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
from flask import Flask, render_template, make_response, request
from flask_script import Manager
from cpu_load import deploy
from name_form import NameForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)


@app.route('/host/cpu', methods=['POST'])
def host_cpu():
    value = request.args.get('value')
    hostname = request.args.get('hostname')
    deploy(hostname)
    response = make_response("<p>hostname: {0}, value: {1}</p>".format(hostname, value), 200)
    return response


@app.route('/control-board', methods=['GET'])
def control_board():
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


@app.route('/form', methods=['GET'])
def form():
    pass


@app.route('/user/<name>', methods=['GET'])
def user(name):
    return render_template('user.html', user=name)


@app.route('/login', methods=['GET'])
def login():
    pass


def main():
    print(os.path.abspath(os.curdir))
    manager.run()

if __name__ == '__main__':
    main()


