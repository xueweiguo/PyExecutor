from ExFramework.ExElement import *
#功能块
class ExFinal(ExElement):
    def __init__(self, name):
        ExElement.__init__(self, name)

    def attach(self, canvas, element_tag, x, y):
        self.canvas = canvas
        self.tag = element_tag
        self.frame = canvas.create_oval(x, y, x + 20, y + 20, tag=self.tag)
        self.frame = canvas.create_oval(x + 5, y + 5, x + 15, y + 15, fill='black', tag=self.tag)