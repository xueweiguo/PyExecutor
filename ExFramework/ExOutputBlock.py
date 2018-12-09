from ExFramework.ExBlock import *


class ExOutputBlock(ExBlock):
    def __init__(self, name, comment):
        ExBlock.__init__(self, name, comment)
        self.append(ExInputPort('Out', '自定义功能输出', self))

    def attach_canvas(self, canvas):
        self.canvas = canvas
        blk_width = 80
        port_height = 10
        port_start = 5
        blk_height = port_start + max(self.countChild(ExInputPort), self.countChild(ExOutputPort)) * port_height
        self.frame = canvas.create_rectangle(self.x, self.y, self.x + blk_width, self.y + blk_height,
                                             tag=self.tag(),
                                             fill='white', outline='black')
        port_y = self.y + port_start
        for port in self.children():
            port.set_position(self.x, port_y)
            port.attach_canvas(canvas)
            port_y = port_y + port_height


