from Foundation.State import *
from ExecutorView import *


class MoveElementState(State):
    def __init__(self, owner, context):
        State.__init__(self, owner, context)

    def entry(self):
        State.entry(self)
        self.context.drawn.handle_request(self.context.drawn, 'drag_begin')

    def event_handling(self, event_type, event):
        if event_type == 'LButtonMove':
            offset_x = event.x - self.context.start.x
            offset_y = event.y - self.context.start.y
            if self.context.drawn:
                self.context.drawn.move(offset_x, offset_y)
                self.context.start = event
                '''
                try:
                    self.context.drawn.move(offset_x, offset_y)
                    self.context.start = event
                except:
                    pass
                '''
        elif event_type == 'LButtonUp':
            self.context.drawn.handle_request(self.context.drawn, 'drag_end')
            self.context.drawn = None
        State.event_handling(self, type, event)

