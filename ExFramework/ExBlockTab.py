from tkinter import *
from tkinter.ttk import *
from ExFramework.ExInputPort import *
from ExFramework.ExPropertyTab import *

class ExBlockTab(ExPropertyTab):
    def __init__(self, parent, name, element):
        ExPropertyTab.__init__(self, parent, name, element)
        self.pack(side=TOP)
        self.tree = Treeview(self)
        self.tree["columns"] = ("名称", "设定值", "说明")
        self.tree.column('#0', minwidth=0, width=0)
        self.tree.column("名称", width=50)  # 表示列,不显示
        self.tree.column("设定值", width=50)
        self.tree.column("说明", width=200)
        self.tree.heading("名称", text="名称")  # 显示表头
        self.tree.heading("设定值", text="设定值")
        self.tree.heading("说明", text="说明")
        r = 0
        for port in self.element().children():
            if isinstance(port, ExInputPort):
                self.tree.insert("", r, text=r+1, values=(port.name(), port.value(), port.comment()))  # 插入数据，
                r = r + 1
        self.tree.pack()




