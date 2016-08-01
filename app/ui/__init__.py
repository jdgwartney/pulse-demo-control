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
from flask import Blueprint, render_template
import logging

logger = logging.getLogger(__name__)

ui = Blueprint('ui', __name__, template_folder='templates', static_folder='static')


@ui.route('/')
def index():
    logger.debug("index()")
    return render_template("index.html")


@ui.route('/login')
def login():
    logger.debug("index()")
    return render_template("login.html")


@ui.route('/scenarios')
def scenarios():
    logger.debug("scenarios()")
    return render_template("scenarios.html")


@ui.route('/scenarios/prototype')
def scenario_prototype():
    logger.debug("scenario_prototype()")
    return render_template("prototype.html")


@ui.route('/scenarios/devops')
def scenario_devops():
    logger.debug("scenario_devops()")
    return render_template("devops.html")


@ui.route('/scenarios/here')
def scenario_here():
    logger.debug("scenario_here()")
    return render_template("here.html")


@ui.route('/control')
def control():
    logger.debug("control()")
    return render_template("control.html")





