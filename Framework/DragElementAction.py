from Foundation.EditAction import *


class DragElementAction(EditAction):
    def __init__(self, element):
        EditAction.__init__(self, element)
        self.memento = element.create_memento()
        # print('org:', self.memento)

    def do(self):
        self.exchange()

    def undo(self):
        self.exchange()

    def exchange(self):
        memento = self.component.create_memento()
        # print('cur:', memento)
        self.component.set_memento(self.memento)
        self.memento = memento
