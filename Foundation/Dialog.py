from tkinter import *

def center_window(wnd):
    width = wnd.winfo_width()
    height = wnd.winfo_height()
    s_width = wnd.winfo_screenwidth()
    s_height = wnd.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (s_width - width) / 2, (s_height - height) / 2)
    wnd.geometry(size)

class ShowDialog(Toplevel):
    def __init__(self, impl, callable):
        Toplevel.__init__(self, takefocus=True)
        self.impl = impl
        self.impl.construct(self)
        self.callable = callable
        self.grab_set()
        self.update()
        center_window(self)

    def close(self):
        self.callable()
        self.destroy()


class TopWnd(Tk):
    def __init__(self, impl):
        Tk.__init__(self, None)
        self.minsize(180, 0)
        self.impl = impl
        self.impl.construct(self)
        self.update()
        center_window(self)

    def close(self):
        self.destroy()


