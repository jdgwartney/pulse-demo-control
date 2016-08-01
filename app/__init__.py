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

from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_log import Logging
from config import config

import logging

bootstrap = Bootstrap()
db = SQLAlchemy()
log = Logging()
logger = logging.getLogger(__name__)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    log.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.ui import ui as ui_blueprint
    app.register_blueprint(ui_blueprint, url_prefix='/ui')

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/v1/api')

#    from app.models import models as models_blueprint
#    app.register_blueprint(models_blueprint)

    logger.debug(app.url_map)

    return app


