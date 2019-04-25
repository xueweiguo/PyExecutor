from Foundation.State import *


class InitialState(State):
    def __init__(self, owner, context):
        State.__init__(self, owner, context)

    def event_handling(self, e_type, event):
        pass

    def entry(self):
        for t in self.transitions:
            t.transition()
            return True
