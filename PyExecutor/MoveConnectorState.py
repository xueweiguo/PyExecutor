from Foundation.State import *
from ExecutorView import *


class MoveConnectorState(State):
    def __init__(self, owner, context):
        State.__init__(self, owner, context)

    def entry(self):
        State.entry(self)
        if self.context.drawn:
            self.context.drawn.drag_begin()
            self.context.drawn.select_segment(self.context.start.x, self.context.start.y)

    def event_handling(self, event_type, event):
        if event_type == 'LButtonMove':
            offset_x = event.x - self.context.start.x
            offset_y = event.y - self.context.start.y
            if self.context.drawn:
                self.context.drawn.move(offset_x, offset_y)
                self.context.start = event
        elif event_type == 'LButtonUp':
            self.context.drawn.drag_end()
            self.context.drawn = None

        State.event_handling(self, type, event)
