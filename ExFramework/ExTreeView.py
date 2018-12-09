from tkinter import *
from tkinter.ttk import *
from ExFramework.ExTreeAccessor import *
from ExFramework.ExObserver import *

class ExTreeView(Frame, ExObserver):
    def __init__(self, parent, accessor, side):
        Frame.__init__(self, parent, relief=GROOVE)
        self.pack(side=side, fill=Y, ipadx=2, ipady=2)
        self.accessor = accessor
        self.accessor.attach_observer(self)
        self.tree = Treeview(self)
        self.tree.heading('#0', text='BlockTree', anchor='w')
        self.build_tree('', self.accessor.get_root())
        self.tree.bind('<<TreeviewSelect>>', self.treeview_select)
        self.tree.pack()

    def build_tree(self, parent, node):
        node_name = self.accessor.get_name(node)
        node_image = self.accessor.get_image(node)
        iid = self.accessor.get_iid(node)
        self.tree.insert(parent, 'end', iid=iid, text=node_name, image =node_image)
        nodes = self.accessor.get_children(node)
        for n in nodes:
            self.build_tree(iid, n)

    def treeview_select(self, event):
        self.accessor.focus(self.tree.focus())

    def update(self, invoker, ext):
        if ext == 'append':
            self.append_node(invoker)
        elif ext == 'remove':
            self.remove_node(invoker)

    def append_node(self, node):
        parent = self.accessor.get_parent(node)
        iid = self.accessor.get_iid(parent)
        self.build_tree(iid, node)

    def remove_node(self, node):
        iid = self.accessor.get_iid(node)
        self.tree.delete(iid)

