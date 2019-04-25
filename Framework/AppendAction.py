from Foundation.EditAction import *


class AppendAction(EditAction):
    def __init__(self, component):
        EditAction.__init__(self, component)
        self.parent = component.parent

    def do(self):
        self.parent.append(self.component)

    def undo(self):
        self.parent.remove(self.component)
