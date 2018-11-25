import sys

sys.path.append('..')

from ExFramework.ExState import *
from ExFramework.ExInputPort import *

class AddConnectorState(ExState):
    def __init__(self, owner, context):
        ExState.__init__(self, owner, context)

    def eventHandling(self, type_str, event):
        if type_str == 'MouseMove':
            self.context.connector.drag_last(event.x, event.y)
        elif type_str == "LButtonDown":
            self.context.connector.append_last()
        elif type_str == "RButtonDown":
            self.context.connector.remove_last()
            if not self.context.connector.line:
                self.context.remove_element(self.context.connector)
                self.context.connector = None
        elif type_str == 'LButtonDoubleClick':
            hit = self.context.find_overlapping(event.x, event.y)
            if hit and isinstance(hit, ExInputPort):
                self.context.connector.setInputPort(hit)
                self.context.connector = None
        ExState.eventHandling(self, type, event)
