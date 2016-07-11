from scenario import Scenario
from cpu_load_action import CPULoadAction


class CPULoadOnWebServer(Scenario):

    def __init__(self, id):
        super(CPULoadOnWebServer, self).__init__(id)

        self._actions[1] = CPULoadAction(1, "52.53.222.210")

    def execute(self, **kwargs):
        action_id = kwargs['action_id']
        action = self._actions[action_id]
        action.run()
