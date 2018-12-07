import sys
import os
import shelve
import json
sys.path.append('..')
from tkinter import * # get widget classes
from tkinter.messagebox import * # get standard dialogs
from tkinter.filedialog import *
from ExFramework.ExTreeView import *
from PyEditorCanvas import *
from PyExecutorFactory import *
from SelModeDlg import *

class PyExecuteWnd(Tk):
    #初始化
    def __init__(self, title, parent=None):
        Tk.__init__(self, parent)
        self.title(title)
        if len(sys.argv) > 1:
            PyExecutorFactory().mode = sys.argv[1]
        else:
            SelModeDlg().mainloop()
        self.center_window(600, 450)
        self.minsize(400, 300)
        self.maxsize(1200, 900)
        self.makemenu()
        self.makeToolbar()
        self.factory = PyExecutorFactory().factory('element')
        self.tree = ExTreeView(self, LEFT)
        self.canvas = PyEditorCanvas(self, self.factory)
        self.canvas.makeToolbar(self.toolbar)
        # 添加图形要素菜单
        add = Menu(self.top, tearoff=False)
        self.canvas.makemenu(add)
        self.top.add_cascade(label='Add', menu=add, underline=0)


    #构建菜单
    def makemenu(self):
        self.top = Menu(self)
        self.config(menu=self.top) # set its menu option

        file = Menu(self.top, tearoff=False)
        file.add_command(label='Open', command=self.load, underline=0)
        file.add_command(label='Save', command=self.save, underline=0)
        file.add_command(label='Quit', command=self.quit, underline=0)
        self.top.add_cascade(label='File', menu=file, underline=0)

        edit = Menu(self.top, tearoff=False)
        edit.add_command(label='delete', command=self.deleteCurrent, underline=0)
        self.top.add_cascade(label='Edit', menu=edit, underline=0)



    def makeToolbar(self):
        self.toolbar = Frame(self, relief=SUNKEN, bd=2)
        self.toolbar.pack(side=TOP, fill=X)


    def save(self):
        mode = PyExecutorFactory().mode
        fn = asksaveasfile(mode='w', filetypes=(("JSON files", "*.json"),("PyExecutor configure data", '*.'+mode)),defaultextension='json')
        if fn:
            f = open(fn.name, 'w', encoding='utf-8')
            dict = {}
            dict['tag_factory'] = ExTagFactory().serialize()
            dict['canvas'] = self.canvas.serialize()
            json.dump(dict, f, cls=PyExecutorFactory().factory('serialize').jsonEncoder(), indent=4)
            f.close()

    def load(self):
        file_name = askopenfilename(filetypes=(("PyExecutor files", "*.pye"),("All files", "*.*")))

    def deleteCurrent(self):
        self.canvas.deleteCurrent()

    def center_window(self, width, height):
        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (s_width - width) / 2, (s_height - height)/2)
        self.geometry(size)

