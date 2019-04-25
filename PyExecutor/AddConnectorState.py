import sys

sys.path.append('..')

from Foundation.State import *
from Framework.InputPort import *

class AddConnectorState(State):
    def __init__(self, owner, context):
        State.__init__(self, owner, context)

    def entry(self):
        State.entry(self)

    def event_handling(self, type_str, event):
        if type_str == 'MouseMove':
            self.context.connector.drag_last(event.x, event.y)
        elif type_str == "LButtonDown":
            self.context.connector.append_last()
        elif type_str == "RButtonDown":
            self.context.connector.remove_last()
            if not self.context.connector.coords:
                self.context.remove_element(self.context.connector)
                self.context.connector.add_cancel()
                self.context.connector = None
        elif type_str == 'LButtonDoubleClick':
            hit = self.context.find_overlapping(event.x, event.y)
            if hit and isinstance(hit, InputPort):
                self.context.connector.attach_input(hit)
                self.context.connector.add_end()
                self.context.connector = None
        State.event_handling(self, type, event)
