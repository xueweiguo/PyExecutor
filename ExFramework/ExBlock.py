from ExFramework.ExElement import *
from ExFramework.ExInputPort import *
from ExFramework.ExOutputPort import *
from ExFramework.ExTagFactory import *
#功能块
class ExBlock(ExElement):
    def __init__(self, name):
        ExElement.__init__(self, name)
        self.tag = ExTagFactory().createTag()

    def attach(self, canvas, x, y):
        self.canvas= canvas
        blk_width = 80
        port_start = 20
        port_height = 10
        blk_height = port_start + max(self.countChild(ExInputPort), self.countChild(ExOutputPort)) * port_height
        self.frame=canvas.create_rectangle(x, y, x+blk_width, y+blk_height, tag=self.tag, \
                                           fill = 'white', outline='black')
        self.caption=canvas.create_text(x + 40, y, tag=self.tag, text=self.name, anchor=N)

        port_y = y + port_start
        for port in self.children:
            if isinstance(port, ExInputPort):
                port.attach(canvas, x, port_y)
                port_y = port_y + port_height

        port_y = y + port_start
        for port in self.children:
            if isinstance(port, ExOutputPort):
                port.attach(canvas, x + blk_width, port_y)
                port_y = port_y + port_height

    def move(self, x, y):
        self.canvas.move(self.tag, x, y)
        for port in self.children:
            port.on_move()

    def set_color(self, color):
        self.canvas.itemconfigure(self.frame, outline=color)

    def serialize(self):
        coords = self.canvas.coords(self.frame)
        dict = ExElement.serialize(self)
        dict.update({'x':coords[0], 'y':coords[1]})
        port_list = []
        for port in self.children:
            port_list.append(port.serialize())
        dict['ports'] = port_list
        return dict

