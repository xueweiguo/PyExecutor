from Foundation.EditAction import *


class MacroAction(EditAction):
    def __init__(self):
        EditAction.__init__(self, None)
        self.actions = []

    def add_action(self, action):
        action.set_level(self.level + 1)
        self.actions.append(action)

    def do(self):
        for c in self.actions:
            c.do()

    def undo(self):
        for c in reversed(self.actions):
            c.undo()

    def __str__(self):
        str = "<MacroAction Begin>\n"
        prefix = ''
        for l in range(0, self.level + 1):
            prefix += '\t'
        for c in self.actions:
            str += prefix +c.__str__() + '\n'
        str += "<MacroAction End>"
        return str

