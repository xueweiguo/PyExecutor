from Foundation.EditAction import *


class MacroAction(EditAction):
    def __init__(self):
        EditAction.__init__(self, None)
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def do(self):
        for c in self.actions:
            c.do()

    def undo(self):
        for c in reversed(self.actions):
            c.undo()
