from ExFramework.ExComponents import *
from ExFramework.ExTagFactory import *

#信息标签
class ExNote(ExComponent):
    def __init__(self):
        ExComponent.__init__(self, '')

    def attach(self, canvas, x, y):
        self.canvas = canvas
        self.frame = canvas.create_rectangle(x, y, x + 100, y + 60, fill='lightyellow', tag=self.tag())