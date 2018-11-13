import sys
sys.path.append('..')
from ExFramework.ExState import *

class PyCanvasMoveElementState(ExState):
    def __init__(self, owner, context):
        ExState.__init__(self, owner, context)

    def eventHandling(self, type, event):
        if type=='LButtonMove':
            offset_x = event.x - self.context.start.x
            offset_y = event.y - self.context.start.y
            if self.context.drawn and len(self.context.drawn) > 0:
                tags = self.context.canvas.gettags(self.context.drawn)
                if len(tags) > 0:
                    self.context.canvas.move(tags[0], offset_x, offset_y)
                    self.context.start = event
        elif type == 'LButtonUp':
            self.context.drawn = None
        ExState.eventHandling(self, type, event)

