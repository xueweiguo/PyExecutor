import sys
from ExFramework.ExState import *
from ExFramework.ExOutputPort import *
from ExFramework.ExComponentFactory import *
from ExFramework.ExTagFactory import *


class IdleState(ExState):
    def __init__(self, owner, context):
        ExState.__init__(self, owner, context)

    def entry(self):
        self.context.drawn = None
        self.context.new_connector = None
        ExState.entry(self)

    def eventHandling(self, event_type, event):
        if event_type == 'LButtonDown':
            self.context.drawn = self.context.find_overlapping(event.x, event.y)
            self.context.set_active(self.context.drawn)
            self.context.start = event
        elif event_type == 'LButtonDoubleClick':
            hit = self.context.find_overlapping(event.x, event.y)
            if hit:
                if isinstance(hit, ExOutputPort):
                    connector = self.context.factory.makeConnector()
                    connector.attach(self.context.canvas)
                    connector.setOutputPort(hit)
                    self.context.connector = connector
            else:
                if self.context.element_type:
                    element = self.context.factory.makeElement(self.context.element_type)
                    element.attach(self.context.canvas, event.x, event.y)
                    self.context.element_dict[element.tag] = element
                    self.context.command = None
                    self.context.canvas.configure(cursor='arrow')
        elif event_type == 'Key':
            pass

        ExState.eventHandling(self, type, event)
