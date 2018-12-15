from ExFramework.ExBlock import *


class ExOutputBlock(ExBlock):
    def __init__(self, parent, name, comment):
        ExBlock.__init__(self, parent, name, comment)

    def construct(self):
        ExBlock.construct(self)
        ExInputPort(self, '', '自定义功能输出').construct()
        return self

    def attach_canvas(self, canvas):
        self._canvas = canvas
        blk_width = 80
        port_height = 10
        port_start = 5
        blk_height = port_start + max(self.countChild(ExInputPort), self.countChild(ExOutputPort)) * port_height
        self._frame = canvas.create_rectangle(self.x, self.y, self.x + blk_width, self.y + blk_height,
                                             tag=self.tag(),
                                             fill='white', outline='black')
        self.caption = canvas.create_text(self.x + 40, self.y, tag=self.tag(), text=self.name(), anchor=N)
        port_y = self.y + port_start
        for port in self.children():
            port.set_position(self.x, port_y)
            port.attach_canvas(canvas)
            port_y = port_y + port_height


