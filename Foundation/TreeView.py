from tkinter import *
from tkinter.ttk import *
from Foundation.TreeAccessor import *
from Foundation.Observer import *


class TreeView(Frame):
    def __init__(self, parent, accessor, side):
        Frame.__init__(self, parent, relief=GROOVE)
        # accessor:提供访问树状数据的接口
        self.accessor = accessor
        # 准备TreeView
        self.tree = Treeview(self)
        self.tree.heading('#0', text='BlockTree', anchor='w')
        self.tree.bind('<<TreeviewSelect>>', self.select_node)
        self.tree.grid(row = 0, column = 0, sticky=W+N+E+S)
        # 垂直滚动条
        vbar = Scrollbar(self, orient=VERTICAL)
        vbar.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=vbar.set)
        vbar.grid(row = 0, column = 1, sticky=N+S)
        hbar = Scrollbar(self, orient=HORIZONTAL)
        hbar.config(command=self.tree.xview)
        self.tree.config(xscrollcommand=hbar.set)
        hbar.grid(row=1, column=0, sticky=E+W)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # 构建表示节点
    def build_tree(self, parent, node, index='end'):
        # 父节点为空时清除已有节点。
        if parent == '':
            top_level = self.tree.get_children()
            if len(top_level):
                self.tree.delete(top_level)
        # 取得节点名
        node_name = self.accessor.get_name(node)
        # 取得节点图标
        node_image = self.accessor.get_image(node)
        # 节点iid
        iid = self.accessor.get_iid(node)
        # 插入节点
        self.tree.insert(parent, index, iid=iid, text=node_name, image =node_image)
        # 取得下级节点
        nodes = self.accessor.get_children(node)
        # 递归生成下级节点
        for n in nodes:
            self.build_tree(iid, n)

    def select_node(self, event):
        self.accessor.focus(self.tree.focus())

    def insert_node(self, node, index):
        parent = self.accessor.get_parent(node)
        iid = self.accessor.get_iid(parent)
        self.build_tree(iid, node, index)

    def append_node(self, node):
        self.insert_node(node, 'end')

    def remove_node(self, node):
        iid = self.accessor.get_iid(node)
        self.tree.delete(iid)

    def update_node(self, node):
        # 取得节点名
        node_name = self.accessor.get_name(node)
        # 取得节点图标
        node_image = self.accessor.get_image(node)
        # 取得节点iid
        iid = self.accessor.get_iid(node)
        # 新节点
        self.tree.item(iid,  text=node_name, image=node_image)

