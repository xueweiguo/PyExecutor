from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from ExFramework.ExElement import *
from ExFramework.ExPropertyTab import *

class ExPropertyDlg:
    def __init__(self, element):
        self.top = Toplevel()
        self.element = element
        self.__notebook = Notebook(self.top)
        self.__notebook.pack(side="top", fill=BOTH, expand=True)
        Button(self.top, text='Apply', command=self.on_apply).pack(side=RIGHT, fill=BOTH)
        Button(self.top, text='Cancel', command=self.on_cancel).pack(side=RIGHT, fill=BOTH)
        self.__tabs = []

    def notebook(self):
        return self.__notebook

    def add_tab(self, tab):
        self.__notebook.add(tab, text=tab.name)
        self.__notebook.pack(side="top", fill=BOTH, expand=True)
        self.__tabs.append(tab)

    def on_apply(self):
        for t in self.__tabs:
            t.apply()
        self.top.quit()
        self.top.destroy()

    def on_cancel(self):
        self.top.quit()
        self.top.destroy()

    def do_modal(self):
        self.top.mainloop()
