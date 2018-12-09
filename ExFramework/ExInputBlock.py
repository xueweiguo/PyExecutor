from ExFramework.ExBlock import *


class ExInputBlock(ExBlock):
    def __init__(self, name, comment):
        ExBlock.__init__(self, name, comment)
        self.append(ExOutputPort('', '自定义模块输入', self))

    def attach_canvas(self, canvas):
        self.canvas= canvas
        blk_width = 80
        port_height = 10
        port_start = 5
        blk_height = port_start + max(self.countChild(ExInputPort), self.countChild(ExOutputPort)) * port_height
        self.frame = canvas.create_rectangle(self.x, self.y, self.x+blk_width, self.y+blk_height, tag=self.tag(),
                                             fill='white', outline='black')
        self.caption = canvas.create_text(self.x + 40, self.y, tag=self.tag(), text=self.name(), anchor=N)

        port_y = self.y + port_start
        for port in self.children():
            if isinstance(port, ExOutputPort):
                port.set_position(self.x + blk_width, port_y)
                port.attach_canvas(canvas)
                port_y = port_y + port_height

