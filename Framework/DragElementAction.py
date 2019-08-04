from Foundation.EditAction import *


class DragElementAction(EditAction):
    def __init__(self, element):
        EditAction.__init__(self, element)
        self.memento = element.create_memento()

    def do(self):
        self.__exchange()

    def undo(self):
        self.__exchange()

    def __exchange(self):
        memento = self.component.create_memento()
        self.component.set_memento(self.memento)
        self.memento = memento
