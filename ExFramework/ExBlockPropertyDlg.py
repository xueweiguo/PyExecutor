from tkinter import *
from tkinter.ttk import *
from ExFramework.ExInputPort import *
from ExFramework.ExPropertyDlg import *

class ExBlockPropertyDlg(ExPropertyDlg):
    def __init__(self, element):
        ExPropertyDlg.__init__(self, element)

    def tabs(self):
        ts = ExPropertyDlg.tabs(self)
        ts.append('ports')
        return ts

    def create_tab(self, title):
        if title == "ports":
            return self.create_port_tab()
        else:
            return ExPropertyDlg.create_tab(self, title)

    def create_port_tab(self):
        tab = Frame(self)
        tab.pack(side=TOP)
        r = 0
        for port in self.element.children:
            if isinstance(port, ExInputPort):
                Label(tab, text=port.name()).grid(row=r, column=0)
                ent = Entry(tab)
                ent.insert(0, port.value())
                ent.grid(row=r, column=1)
                r = r + 1
        return tab




