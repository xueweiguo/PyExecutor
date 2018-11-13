from ExFramework.ExState import *

class ExInitialState(ExState):
    def __init__(self, owner, context):
        ExState.__init__(self, owner, context)

    def eventHandling(self, event):
        pass

    def entry(self):
        for t in self.transitions:
            t.transition()
            return True
