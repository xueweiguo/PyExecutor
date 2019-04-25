from Foundation.EditAction import *
from Framework.OutputPort import *


class AttachConnectorAction(EditAction):
    def __init__(self, output_port, connector):
        EditAction.__init__(self, output_port)
        self.connector = connector

    def do(self):
        self.component.attach_connector(self.connector)
        self.connector.attach_output(self.component)

    def undo(self):
        self.component.detach_connector(self.connector)
        self.connector.attach_output(None)
