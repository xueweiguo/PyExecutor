import os
import shelve
import threading
from tkinter import * # get widget classes
from tkinter.filedialog import *
from tkinter.messagebox import * # get standard dialogs

from Framework.DiagramWnd import *
from DiagramTreeAccessor import DiagramTreeAccessor
from ObserverAdapter import *
from ExecutorView import *


class ExecutorWnd(DiagramWnd):
    # 初始化
    def __init__(self, title, parent=None):
        self.file = None
        DiagramWnd.__init__(self, title, parent)

    def create_view(self):
        # 构建TreeView,并准备接收通知
        self.tree = TreeView(self, DiagramTreeAccessor(self), LEFT)
        # 构建编辑区,并准备接收通知
        self.view = ExecutorView(self, ObserverAdapter(self))

    # 构建菜单
    def make_menu(self):
        self.top_menu = Menu(self)
        self.config(menu=self.top_menu) # set its menu option

        self.file = Menu(self.top_menu, tearoff=False)
        self.file.add_command(label='New', command=self.new, underline=0)
        self.file.add_command(label='Open', command=self.load, underline=0)
        self.file.add_command(label='Save', command=self.save, underline=0)
        self.file.add_command(label='Info', command=self.info, underline=0)
        self.file.add_command(label='Quit', command=self.exit, underline=0)
        self.top_menu.add_cascade(label='File', menu=self.file, underline=0)

    def make_toolbar(self):
        self.edit_bar = Frame(self, relief=SUNKEN, bd=2)
        self.edit_bar.pack(side=TOP, fill=X)
        self.toolbar = Frame(self, relief=SUNKEN, bd=2)
        self.toolbar.pack(side=TOP, fill=X)

    def info(self):
        self.view.show_info()








