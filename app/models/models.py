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
    commands = db.relationship('Command', backref='Action', lazy='dynamic')
    scenario_id = db.Column(db.Integer, db.ForeignKey('scenarios.id'))

    def __repr__(self):
        return "Action({0}, '{1}', {2})".format(self.id, self.name, self.scenario_id)


class Command(db.Model):

    __tablename__ = 'commands'

    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(64), unique=True)
    cmd = db.Column(db.String(64))
    args = db.Column(db.String(128))
    action_id = db.Column(db.Integer, db.ForeignKey('actions.id'))

    def __repr__(self):
        return "Command({0}, '{1}', '{2}', '{3}', {4})".format(
            self.id, self.name, self.cmd, self.args, self.action_id)


class Scenario(db.Model):

    __tablename__ = 'scenarios'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    actions = db.relationship('Action', backref='Scenario', lazy='dynamic')

    def __repr__(self):
        return "Scenario({0}, '{1}')".format(self.id, self.name)
