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


class Action(db.Model):

    __tablename__ = 'actions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    vals = db.Column(db.String(128), unique=True)
    #commands = models.relationship('Command', backref='primaryjoin')

    def __repr__(self):
        return "<Action('{0}', '{1}')".format(self.name, self.vals)


class Command(db.Model):

    __tablename__ = 'commands'

    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(64), unique=True)
    cmd = db.Column(db.String(64))
    args = db.Column(db.String(128))

    def __repr__(self):
        return "Command('{0}', '{1}')".format(self.name, self.args)


class Scenario(db.Model):
    __tablename__ = 'scenarios'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # actions = models.relationship('Action', backref='role', lazy='dynamic')

    def __repr__(self):
        return "<Command('{0}', '{1}')".format(self.name, self.values)