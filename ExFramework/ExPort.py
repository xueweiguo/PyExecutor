from ExFramework.ExComponent import *

#信息标签
class ExPort(ExComponent):
    def __init__(self, name, comment, owner):
        ExComponent.__init__(self, name, comment)
        self.owner = owner
        self.x = None
        self.y = None

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_color(self, color):
        self.canvas.itemconfigure(self.frame, outline=color)

    def accept(self, visitor):
        pass

    def value(self):
        return 0


