import json
from ExFramework.ExComponent import *

#信息标签
class ExPort(ExComponent):
    def __init__(self, parent, name, comment):
        ExComponent.__init__(self, parent, name, comment)
        self.x = None
        self.y = None

    def construct(self):
        self.tag = self.parent.tag
        self.parent.append(self)
        return self

    def detach_canvas(self):
        self._canvas.delete(self._frame)
        self._frame = None
        self._canvas.delete(self.caption)
        self.caption = None
        ExComponent.detach_canvas(self)

    def set_color(self, color):
        self._canvas.itemconfigure(self._frame, outline=color)

    def value(self):
        return 0

    def set_value(self, v):
        return 0

    @staticmethod
    def height():
        return 10


