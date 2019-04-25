from Foundation.EditAction import *

class RemoveAction(EditAction):
    def __init__(self, component, index):
        EditAction.__init__(self, component)
        self.parent = component.parent
        self.index = index

    def do(self):
        self.parent.remove(self.component)

    def undo(self):
        self.parent.insert(self.component, self.index)