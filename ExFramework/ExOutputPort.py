from ExFramework.ExPort import *

#信息标签
class ExOutputPort(ExPort):
    def __init__(self, parent, name, comment):
        ExPort.__init__(self, parent, name, comment)
        self.caption = None
        self.x = None
        self.y = None
        self.connectors = []

    def attach_canvas(self, canvas):
        self.canvas = canvas
        self.frame = canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 5, fill='cyan',
                                             tags=[self.parent().tag(), self.name()])
        self.caption = canvas.create_text(self.x - 2, self.y, tag=self.parent().tag(), text=self.name(), anchor=E)

    def detach_canvas(self):
        self.canvas.delete(self.frame)
        self.frame = None
        self.canvas.delete(self.caption)
        self.caption = None
        ExPort.detach_canvas(self)

    def point(self):
        bound_rect = self.canvas.coords(self.frame)
        pos = []
        pos.append(bound_rect[2])
        pos.append((bound_rect[1] + bound_rect[3])/2)
        return pos

    def add_connector(self, c):
        self.connectors.append(c)

    def remove_connector(self, c):
        self.connectors.remove(c)

    def on_move(self):
        for c in self.connectors:
            coords = self.point()
            c.move_first(coords[0], coords[1])

    def accept(self, visitor):
        visitor.visitOutputPort(self)

