from Foundation.EditAction import *


class DetachConnectorAction(EditAction):
    def __init__(self, output_port, connector):
        EditAction.__init__(self, output_port)
        self.connector = connector

    def do(self):
        self.component.detach_connector(self.connector)

    def undo(self):
        self.component.attach_connector(self.connector)
