import copy
from Foundation.EditAction import *


class ChangeMemberAction(EditAction):
    def __init__(self, component, getter, setter):
        EditAction.__init__(self, component)
        self.getter = getter
        self.setter = setter
        prev = getter(self.component)
        self.member = copy.copy(prev)

    def do(self):
        self.__exchange()

    def undo(self):
        self.__exchange()

    def __exchange(self):
        temp = self.getter(self.component)
        self.setter(self.component, self.member)
        self.member = temp
