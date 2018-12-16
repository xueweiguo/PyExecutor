from ExFramework.ExPort import *

#输入端口
class ExInputPort(ExPort):
    def __init__(self, parent, name, comment):
        ExPort.__init__(self, parent, name, comment)
        self.connector = None
        self.caption = None

    def attach_canvas(self, canvas):
        self.calculate_position()
        self._frame = canvas.create_rectangle(self.x - 10, self.y, self.x, self.y + 5,
                                              fill='cyan', tags=[self.parent().tag(), self.name()])
        self.caption = canvas.create_text(self.x + 2, self.y,
                                          tag=self.parent().tag(), text=self.name(), anchor=W)
        ExPort.attach_canvas(self, canvas)

    def point(self):
        bound_rect = self._canvas.coords(self._frame)
        pos = []
        pos.append(bound_rect[0])
        pos.append((bound_rect[1] + bound_rect[3])/2)
        return pos

    def set_connector(self, c):
        self.connector = c

    def move(self):
        coords = self.point()
        if self.connector:
            self.connector.move_last(coords[0], coords[1])

    def serialize(self):
        return ExPort.serialize(self)

    def calculate_position(self):
        block = self.parent()
        port_y = block.port_start()
        for port in block.children():
            if isinstance(port, ExInputPort):
                if port == self:
                    self.x = block.left()
                    self.y = port_y
                port_y = port_y + self.height()

