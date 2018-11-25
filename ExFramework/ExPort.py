from ExFramework.ExComponents import *

#信息标签
class ExPort(ExComponent):
    def __init__(self, name, owner):
        ExComponent.__init__(self, name)
        self.owner = owner

    def set_color(self, color):
        self.canvas.itemconfigure(self.frame, outline=color)


