from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from ExFramework.ExElement import *
from ExFramework.ExPropertyTab import *

class ExPropertyDlg:
    def __init__(self, element):
        self.top = Toplevel()
        self.element = element
        self.__notebook__ = Notebook(self.top)
        self.__notebook__.pack(side="top", fill=BOTH, expand=True)
        Button(self.top, text='Apply', command=self.on_apply).pack(side=RIGHT, fill=BOTH)
        Button(self.top, text='Cancel', command=self.on_cancel).pack(side=RIGHT, fill=BOTH)

    def notebook(self):
        return self.__notebook__

    def add_tab(self, tab):
        self.__notebook__.add(tab, text=tab.name)
        self.__notebook__.pack(side="top", fill=BOTH, expand=True)

    def on_apply(self):
        for t in self.tabs():
            t.apply()
        self.top.quit()
        self.top.destroy()

    def on_cancel(self):
        self.top.quit()
        self.top.destroy()

    def do_modal(self):
        self.top.mainloop()
