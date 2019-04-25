import abc


class EditAction(metaclass=abc.ABCMeta):
    def __init__(self, component):
        self.component = component

    @abc.abstractmethod
    def do(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


