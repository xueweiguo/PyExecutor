import sys
from ExFramework.ExState import *
from PyEditorCanvas import *


class MoveLineState(ExState):
    def __init__(self, owner, context):
        ExState.__init__(self, owner, context)

    def entry(self):
        ExState.entry(self)
        if self.context.drawn:
            self.context.drawn.select_segment(self.context.start.x, \
                                              self.context.start.y)

    def eventHandling(self, event_type, event):
        if event_type == 'LButtonMove':
            offset_x = event.x - self.context.start.x
            offset_y = event.y - self.context.start.y
            if self.context.drawn:
                self.context.drawn.move(offset_x, offset_y)
                self.context.start = event
        elif event_type == 'LButtonUp':
            self.context.drawn = None

        ExState.eventHandling(self, type, event)
