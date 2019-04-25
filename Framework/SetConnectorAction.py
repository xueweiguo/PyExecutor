from Foundation.EditAction import *


class SetConnectorAction(EditAction):
    def __init__(self, input_port, prev_connector, new_connector):
        EditAction.__init__(self, input_port)
        self.prev = prev_connector
        self.new = new_connector

    def do(self):
        self.component.set_connector(self.new)
        if self.new:
            self.new.attach_input(self.component)
        elif self.prev:
            self.prev.attach_input(None)

    def undo(self):
        self.component.set_connector(self.prev)
        if self.prev:
            self.prev.attach_input(self.component)
        elif self.new:
            self.new.attach_input(None)
