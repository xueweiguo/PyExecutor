from tkinter.ttk import *
from ExFramework.ExOutputPort import *
from ExFramework.ExPropertyTab import *

class MathFunTab(ExPropertyTab):
    def __init__(self, parent, name, element):
        ExPropertyTab.__init__(self, parent, name, element)
        self.pack(side=TOP)
        self.tree = Treeview(self)
        self.tree["columns"] = ("输出", "表达式", "说明")
        self.tree.column('#0', minwidth=0, width=0)
        self.tree.column("输出", width=50)  # 表示列,不显示
        self.tree.column("表达式", width=100)
        self.tree.column("说明", width=100)
        self.tree.heading("输出", text="输出")  # 显示表头
        self.tree.heading("表达式", text="表达式")
        self.tree.heading("说明", text="说明")
        r = 0
        for port in self.element.children():
            if isinstance(port, ExOutputPort):
                self.tree.insert("", r, text=r + 1, values=(port.name, "", port.comment))  # 插入数据，
                r = r + 1
        self.tree.pack()
