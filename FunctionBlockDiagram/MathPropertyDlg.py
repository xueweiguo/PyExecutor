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
        self.tree = Treeview(tab, show='tree')
        self.tree["columns"] = ("名称", "设定值", "说明")
        self.tree.column('#0', minwidth=0, width=0)
        self.tree.column("名称", width=50)  # 表示列,不显示
        self.tree.column("设定值", width=100)
        self.tree.column("说明", width=100)
        self.tree.heading("名称", text="名称")  # 显示表头
        self.tree.heading("设定值", text="设定值")
        self.tree.heading("说明", text="说明")
        r = 0
        for port in self.element.children:
            if isinstance(port, ExOutputPort):
                self.tree.insert("", r, text=r + 1, values=(port.name(), "", port.comment()))  # 插入数据，
                r = r + 1
        self.tree.pack()
        return tab