from application.api.scenarios.action import Action
from application.api.control.cpu_load import cpu_load


class CPULoadAction(Action):

    def __init__(self, id, host=None):
        super(CPULoadAction, self).__init__(id)
        self._host = host

    def run(self):
        cpu_load(self._host)
