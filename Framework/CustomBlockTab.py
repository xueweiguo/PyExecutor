from tkinter import *
from tkinter.ttk import *
from Foundation.ListView import *
from Framework.PropertyTab import PropertyTab
from Framework.CustomBlock import *


class CustomBlockTab(PropertyTab):
    def __init__(self, parent, name, element):
        PropertyTab.__init__(self, parent, name, element)
        self.cur_tag = 0
        self.pack(side=TOP)
        toolbar = Frame(self, relief=SUNKEN)
        Button(toolbar, text="Add Input", command=self.add_input).pack(side=LEFT)
        Button(toolbar, text="Add Output", command=self.add_output).pack(side=LEFT)
        self.delete_btn = Button(toolbar, text="Delete", command=self.delete_current)
        self.delete_btn.configure(state ='disabled')
        self.delete_btn.pack(side=LEFT)
        toolbar.pack(side=TOP, fill=X)
        # 自定义功能块输入、输出端口表示
        self.list = ListView(self, ("ID", '类型', '位置', '名称', '设定值', '说明'))
        # 设置列宽
        self.list.config_column("ID", 50)
        self.list.config_column("类型", 7 * 8)
        self.list.config_column("位置", 2 * 8, True)
        self.list.config_column("名称", 100, True)
        self.list.config_column("设定值", 50, True)
        self.list.config_column("说明", 200, True)
        self.list.pack()

        self.items = dict()
        for port in self.element.iter('input_port'):
            self.list.insert("", 'end', iid=port.tag, values=(port.tag, 'Input', port.pos, port.name, port.value, port.comment))
        for port in self.element.iter('output_port'):
            self.list.insert("", 'end', iid=port.tag, values=(port.tag, 'Output', port.pos, port.name, port.value, port.comment))
        self.sort()
        self.current = None
        self.edit = None

    def add_input(self):
        tag = self.get_tag()
        self.list.insert("", 'end', iid=tag, values=(tag, 'Input', -1, 'NoName', '', ''))
        self.sort()

    def add_output(self):
        tag = self.get_tag()
        self.list.insert("", 'end', iid=tag, values=(tag, 'Output', -1, 'NoName', '', ''))
        self.sort()

    def delete_current(self):
        current = self.list.focus()
        if current:
            self.list.delete(current)
            self.delete_btn.configure(state ='disabled')

    def get_tag(self):
        tag = "T{:d}".format(self.cur_tag)
        self.cur_tag = self.cur_tag + 1
        return tag

    def item_selected(self, event):
        delete_enable = False
        focus = self.focus()
        if focus:
            prefix = focus[0:1]
            if prefix != 'T':
                port = self.element.dict[focus]
                if port.conencted:
                    return
        self.delete_btn.configure(state='normal')

    def apply(self):
        remove_list = []
        for port in self.element.iter():
            if self.list.exists(port.tag):
                values = self.list.set(port.tag)
                if port.pos != int(values['位置']):
                    port.pos = int(values['位置'])
                if port.name != values['名称']:
                    port.name = values['名称']
                if port.value != values['设定值']:
                    port.value = values['设定值']
                if port.comment != values['说明']:
                    port.set_comment(values['说明'])
            else:
                remove_list.append(self.element.dict[port.tag])
        for port in remove_list:
            self.element.remove(port)

        for iid in self.list.get_children(''):
            if iid[0:1] == 'T':
                values = self.list.set(iid)
                if values['类型'] == 'Input':
                    self.element.append_input(int(values['位置']), values['名称'], values['说明'])
                else:
                    self.element.append_output(int(values['位置']), values['名称'], values['说明'])
        self.element.resize()

    def sort(self):
        self.list.sort_column(['#2', '#3'], False)




