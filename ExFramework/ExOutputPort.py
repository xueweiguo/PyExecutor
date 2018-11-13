from ExFramework.ExPort import *

#信息标签
class ExOutputPort(ExPort):
    def __init__(self, name, owner):
        ExPort.__init__(self, name, owner)

    def attach(self, canvas, x, y):
        self.canvas = canvas
        self.frame = canvas.create_rectangle(x, y, x + 10, y + 5, fill='lightcyan', tags=[self.owner.tag, self.name])
        self.caption = canvas.create_text(x - 2, y, tag=self.owner.tag, text=self.name, anchor=E)

    def connectPoint(self):
        bound_rect = self.canvas.coords(self.frame)
        pos = []
        pos.append(bound_rect[2])
        pos.append((bound_rect[1] + bound_rect[3])/2)
        return pos

