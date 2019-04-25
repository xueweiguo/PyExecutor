from tkinter import *
from tkinter.ttk import *
from Framework.InputPort import *
from Framework.PropertyTab import *
from Foundation.ListView import *

class BlockTab(PropertyTab):
    def __init__(self, parent, name, element):
        PropertyTab.__init__(self, parent, name, element)
        self.pack(side=TOP)
        # 自定义功能块输入、输出端口表示
        self.list = ListView(self, ('名称', '设定值', '说明'))
        # 设置列宽
        self.list.config_column("名称", 50)
        self.list.config_column("设定值", 50, True)
        self.list.config_column("说明", 250)
        self.list.pack()

        self.items = dict()
        for port in self.element.iter('input_port'):
            if not port.connector:
                self.list.insert("", 'end', iid=port.tag, values=(port.name, port.value, port.comment))
        self.current = None
        self.edit = None

    def apply(self):
        for port in self.element.iter('input_port'):
            if not port.connector:
                values = self.list.set(port.tag)
                if port.value != values['设定值']:
                    port.value = values['设定值']





