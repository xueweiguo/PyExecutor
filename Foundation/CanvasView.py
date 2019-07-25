from tkinter import *


class CanvasView(Frame):
    def __init__(self, parent=None, color='lightyellow'):
        Frame.__init__(self, parent)
        canv = Canvas(self, bg=color, relief=SUNKEN)
        canv.config(width=600, height=400)
        canv.config(scrollregion=(0, 0, 1500, 1000))
        canv.config(highlightthickness=0)
        canv.focus_set()
        canv.grid(row=0, column=0, sticky=W+N+E+S)

        canv.bind('<Double-1>', self.onDoubleClick)
        canv.bind('<ButtonPress-1>', self.onLButtonDown)
        canv.bind('<ButtonPress-3>', self.onRButtonDown)
        canv.bind('<B1-Motion>', self.onLButtonMove)
        canv.bind('<Motion>', self.onMouseMove)
        canv.bind('<ButtonRelease-1>', self.onLButtonUp)
        canv.bind('<Key>', self.onKey)

        vbar = Scrollbar(self, orient=VERTICAL)
        vbar.config(command=canv.yview)
        canv.config(yscrollcommand=vbar.set)
        vbar.grid(row=0, column=1, sticky=N+S)

        hbar = Scrollbar(self, orient=HORIZONTAL)
        hbar.config(command=canv.xview)
        canv.config(xscrollcommand=hbar.set)
        hbar.grid(row=1, column=0, sticky=W+E)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

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

