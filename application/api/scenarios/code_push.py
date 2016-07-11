from application.api.scenarios.cpu_load import Scenario


class BadCodePush(Scenario):

    def __init__(self, id):
        super(BadCodePush, self).__init__(id)

    def execute(self, **kwargs):
        pass
