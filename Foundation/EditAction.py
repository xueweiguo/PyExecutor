import abc


class EditAction(metaclass=abc.ABCMeta):
    def __init__(self, component):
        self.component = component
        self.level = 0

    def set_level(self, level):
        self.level = level

    @abc.abstractmethod
    def do(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


