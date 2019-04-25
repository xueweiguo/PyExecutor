import json
from Framework.Component import *


#数据端口
class DataPort(Component):
    def __init__(self, cd, pos, name, comment):
        Component.__init__(self, cd, name, comment)
        self.x = None
        self.y = None
        self.pos = pos
        self.__value = 0

    def construct(self, parent):
        Component.construct(self, parent)
        if parent.canvas:
            self.attach_canvas(parent.canvas)
        parent.append(self)
        return self

    def detach_canvas(self):
        self.canvas.delete(self.frame)
        self.canvas.delete(self.caption)
        Component.detach_canvas(self)

    def set_color(self, color):
        self.canvas.itemconfigure(self.frame, outline=color)

    @property
    def value(self):
        return self.get_value()

    @value.setter
    def value(self, v):
        self.set_value(v)

    @staticmethod
    def height():
        return 16

    @property
    def id(self):
        return self.parent.tag + '.' + self.name

    @property
    def frame(self):
        return self.tag + '.frame'

    @property
    def caption(self):
        return self.tag + '.caption'

    def name_changed(self):
        try:
            self.canvas.itemconfigure(self.caption, text=self.name)
        except:
            pass  # do nothing

    def comment_changed(self):
        pass

    def get_value(self):
        return self.__value

    def set_value(self, v):
        self.handle_request(self, 'change_member',
                            {'getter': DataPort.get_value,
                             'setter': DataPort.set_value,
                             'cur': self.__value,
                             'new': v})
        self.__value = v

