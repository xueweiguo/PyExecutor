from tkinter import *


class ShowDialog(Toplevel):
    def __init__(self, impl, callable):
        Toplevel.__init__(self, takefocus=True)
        self.impl = impl
        self.impl.construct(self)
        self.callable = callable
        self.grab_set()

    def close(self):
        self.callable()
        self.destroy()


class TopWnd(Tk):
    def __init__(self, impl):
        Tk.__init__(self)
        self.impl = impl
        self.impl.construct(self)

    def close(self):
        self.destroy()


