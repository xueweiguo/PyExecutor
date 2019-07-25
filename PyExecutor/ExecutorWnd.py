import os
import shelve
import threading
from tkinter import * # get widget classes
from tkinter.filedialog import *
from tkinter.messagebox import * # get standard dialogs

from Framework.DiagramWnd import *
from PyExecutor.DiagramTreeAccessor import DiagramTreeAccessor
from PyExecutor.ExecutorMediator import *
from PyExecutor.ExecutorView import *


# 主窗口
class ExecutorWnd(DiagramWnd):
    # 初始化
    def __init__(self, title, parent=None):
        self.file = None
        # 构建中介者
        self.mediator = ExecutorMediator(self)
        DiagramWnd.__init__(self, title, parent)

    # 构建Tree View和编辑区
    def create_view(self):
        paned_window = PanedWindow(self, sashpad=0, sashrelief=RAISED)
        # 构建TreeView,并准备接收通知
        self.tree = TreeView(paned_window, DiagramTreeAccessor(self.mediator), LEFT)
        paned_window.add(self.tree)
        # 构建编辑区,并准备接收通知
        self.view = ExecutorView(self, self.mediator)
        paned_window.add(self.view)
        paned_window.grid(row=2, column=0, sticky=W+N+E+S)
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
        self.edit_bar.grid(row=0, column=0, sticky=W)
        self.toolbar = Frame(self, relief=SUNKEN, bd=2)
        self.toolbar.grid(row=1, column=0, sticky=W)

    def info(self):
        self.view.show_info()








