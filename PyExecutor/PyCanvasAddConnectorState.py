import sys
import math
sys.path.append('..')

from ExFramework.ExState import *
from ExFramework.ExInputPort import *

class PyCanvasAddConnectorState(ExState):
    def __init__(self, owner, context):
        ExState.__init__(self, owner, context)

    def eventHandling(self, type, event):
        if type=='MouseMove':
            self.context.connector.moveLastPoint(event.x, event.y)
        elif type == "LButtonDown":
            self.context.connector.appendPoint()
        elif type == "RButtonDown":
            self.context.connector.removeLastPoint()
            if not self.context.connector.line:
                del self.context.connector
                self.context.connector = None
        elif type == 'LButtonDoubleClick':
            hit_id = self.context.canvas.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)
            if len(hit_id) > 0:
                tags = self.context.canvas.gettags(hit_id)
                hit = self.context.findComponent(tags)
                if isinstance(hit, ExInputPort):
                    self.context.connector.setInputPort(hit)
                    self.context.element_dict[self.context.connector.tag] = self.context.connector
                    self.context.connector = None
        ExState.eventHandling(self, type, event)
