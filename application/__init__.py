# Copyright 2015 BMC Software, Inc.
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
from application.ui import uis
from application.api import apis
from flask_log import Logging
import logging
import os
from application.db.command import Command

logger = logging.getLogger(__name__)

app = Flask(__name__)

app.config['FLASK_LOG_LEVEL'] = 'DEBUG'
flask_log = Logging(app)

Bootstrap(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join( basedir, 'data.sqlite')
db = SQLAlchemy(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def root():
    return redirect('/ui')

app.register_blueprint(apis, url_prefix='/v1/api')
app.register_blueprint(uis, url_prefix='/ui')


logger.debug(app.url_map)

