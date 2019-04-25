from tkinter import *
from Framework.ExecCanvas import *


class ScrollCanvas(Frame):
    def __init__(self, parent=None, canvas=None, color='lightyellow'):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        canv = canvas(self, bg=color, relief=SUNKEN)
        canv.config(width=300, height=200)
        canv.config(scrollregion=(0, 0, 300, 1000))
        canv.config(highlightthickness=0)
        canv.focus_set()

        sbar = Scrollbar(self)
        sbar.config(command=canv.yview)
        canv.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        canv.pack(side=LEFT, expand=YES, fill=BOTH)

        canv.bind('<Double-1>', self.onDoubleClick)
        canv.bind('<ButtonPress-1>', self.onLButtonDown)
        canv.bind('<ButtonPress-3>', self.onRButtonDown)
        canv.bind('<B1-Motion>', self.onLButtonMove)
        canv.bind('<Motion>', self.onMouseMove)
        canv.bind('<ButtonRelease-1>', self.onLButtonUp)
        canv.bind('<Key>', self.onKey)

        self.canvas = canv

    def onDoubleClick(self, event):
        raise NotImplementedError

    def onLButtonDown(self, event):
        raise NotImplementedError

    def onRButtonDown(self, event):
        raise NotImplementedError

    def onLButtonMove(self, event):
        raise NotImplementedError

    def onMouseMove(self, event):
        raise NotImplementedError

    def onLButtonUp(self, event):
        raise NotImplementedError

    def onKey(self, event):
        raise NotImplementedError

