import sys
sys.path.append('..')
from ExFramework.ExState import *
from ExFramework.ExOutputPort import *
from ExFramework.ExComponentFactory import *
from ExFramework.ExTagFactory import *

class PyCanvasIdleState(ExState):
    def __init__(self, owner, context):
        ExState.__init__(self, owner, context)

    def entry(self):
        self.context.drawn = None
        self.context.new_connector = None
        ExState.entry(self)

    def eventHandling(self, type, event):
        if type=='LButtonDown':
            self.context.drawn = self.context._canvas.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)
            if len(self.context.drawn) > 0:
                tags = self.context._canvas.gettags(self.context.drawn)
                if len(tags) > 0:
                    self.context.start = event
            else:
                self.context.drawn = None
        elif type=='LButtonDoubleClick':
            hit_id = self.context.canvas.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)
            if len(hit_id) > 0:
                tags = self.context.canvas.gettags(hit_id)
                hit = self.context.findComponent(tags)
                if isinstance(hit, ExOutputPort):
                    connector = self.context.factory.makeConnector()
                    connector.attach(self.context.canvas)
                    connector.setOutputPort(hit)
                    self.context.connector = connector
            else:
                if self.context.element_type != None:
                    element=self.context.factory.makeElement(self.context.element_type)
                    element.set_position(event.x, event.y)
                    element.attach_canvas(self.context.canvas)
                    self.context.element_dict[element.tag] = element
                    self.context.command = None
                    self.context.canvas.configure(cursor='arrow')
        ExState.eventHandling(self, type, event)