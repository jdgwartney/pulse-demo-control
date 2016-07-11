from scenario import Scenario
from cpu_load_action import CPULoadAction


class CPULoadOnWebServer(Scenario):

    def __init__(self, id):
        super(CPULoadOnWebServer, self).__init__(id)

        self._actions[1] = CPULoadAction(1, "52.52.34.20")

    def execute(self, action_id):
        action = self._actions[int(action_id)]
        action.run()
