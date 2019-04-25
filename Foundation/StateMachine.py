from Foundation.State import *


class StateMachine:
    def __init__(self, owner, context):
        self.context = context
        self.active = None
        self.initial = None

    def entry(self):
        self.active = self.initial
        if self.active:
            self.active.entry()

    def event_handling(self, e_type, event):
        if self.active:
            return self.active.event_handling(e_type, event)

    def exit(self):
        pass
