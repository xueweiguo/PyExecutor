from ExFramework.ExPort import *

#信息标签
class ExInputPort(ExPort):
    def __init__(self, name, owner):
        ExPort.__init__(self, name, owner)
        self.connector = None
        self.caption = None

    def attach(self, canvas, x, y):
        self.canvas = canvas
        self.frame = canvas.create_rectangle(x - 10, y, x, y + 5, fill='cyan', tags=[self.owner.tag, self.name])
        self.caption = canvas.create_text(x + 2, y, tag=self.owner.tag, text=self.name, anchor=W)

    def point(self):
        bound_rect = self.canvas.coords(self.frame)
        pos = []
        pos.append(bound_rect[0])
        pos.append((bound_rect[1] + bound_rect[3])/2)
        return pos

    def set_connector(self, c):
        self.connector = c

    def on_move(self):
        coords = self.point()
        if self.connector:
            self.connector.move_last(coords[0], coords[1])

    def serialize(self):
        return ExPort.serialize(self)

