from ExFramework.ExOutputPort import *
from ExFramework.ExBlockPropertyDlg import *


class MathPropertyDlg(ExBlockPropertyDlg):
    def __init__(self, element):
        ExBlockPropertyDlg.__init__(self, element)

    def tabs(self):
        ts = ExBlockPropertyDlg.tabs(self)
        ts.append('expression')
        return ts

    def create_tab(self, title):
        if title == "expression":
            return self.create_expr_tab()
        else:
            return ExBlockPropertyDlg.create_tab(self, title)

    def create_expr_tab(self):
        tab = Frame(self)
        tab.pack(side=TOP)
        r = 0
        for port in self.element.children:
            if isinstance(port, ExOutputPort):
                Label(tab, text=port.name()).grid(row=r, column=0)
                ent = Entry(tab)
                #ent.insert(0, port.name())
                ent.grid(row=r, column=1)
                r = r + 1
        return tab