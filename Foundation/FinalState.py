from Foundation.State import *


class FinalState(State):
    def __init__(self, owner, context):
        State.__init__(self, owner, context)

    def event_handling(self, e_type, event):
        pass

    def entry(self):
        self.exit()


