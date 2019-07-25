import os
import shelve
import threading
from tkinter import * # get widget classes
from tkinter.filedialog import *
from tkinter.messagebox import * # get standard dialogs

from Foundation.TreeView import *
from Foundation.Dialog import *
from Foundation.TreeAccessor import *
from Framework.TopDiagram import *
from Framework.DiagramView import *
from Framework.SelectDiagramType import *


class DiagramWnd(Tk):
    # 初始化
    def __init__(self, title, parent):
        Tk.__init__(self, parent)
        self.title(title)
        self.center_window(800, 500)
        self.minsize(400, 300)
        self.maxsize(1200, 900)
        # 处理Windows关闭主窗口消息
        self.protocol("WM_DELETE_WINDOW", self.exit)

        self.context = None

        self.top_menu = None
        self.edit_bar = None
        self.toolbar = None

        # 构建工具条
        self.make_menu()
        # 构建菜单栏
        self.make_toolbar()
        self.create_view()
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # 构建新逻辑
        self.new(False)

    def create_view(self):
        raise NotImplementedError

    # 构建菜单
    def make_menu(self):
        raise NotImplementedError

    def make_toolbar(self):
        raise NotImplementedError

    def new(self, sel_type = True):
        if self.ask_clear():
            if sel_type:
                ShowDialog(SelectDiagramType(), self.__new)
            else:
                self.__new()

    def __new(self):
        self.view.new()
        self.tree.build_tree('', self.view.top_diagram)

    def save(self):
        fn = self.ask_save_name()
        if fn:
            self.view.save(fn)
            return True
        else:
            return False

    def load(self):
        if self.ask_clear():
            fn = self.ask_load_name()
            if fn:
                self.view.load(fn)
                self.tree.build_tree('', self.view.top_diagram)

    def exit(self):
        if self.ask_clear():
            self.view.stop_debug()
            self.quit()

    def ask_clear(self):
        if self.view.modified():
            confirm = askyesnocancel("Save?", "The diagram has been modified, do you want to save it?")
            if confirm is None: # Cancel
                return False
            elif confirm:  #Yes
                return self.save()
            else: #No
                return True
        else:
            return True

    def ask_save_name(self):
        return asksaveasfile(mode='w', filetypes=(("JSON files", "*.json" ),
                            ("PyExecutor configure data", '*.' + self.view.type)),
                           defaultextension='json')

    def ask_load_name(self):
        return askopenfile(mode='r', filetypes=(("JSON files", "*.json"),
                        ("PyExecutor configure data", '*.' + self.view.type)),
                         defaultextension='json')

    def center_window(self, width, height):
        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (s_width - width) / 2, (s_height - height) / 2)
        self.geometry(size)
