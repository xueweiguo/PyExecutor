import sys
import os
import shelve
import json
sys.path.append('..')
from tkinter import * # get widget classes
from tkinter.messagebox import * # get standard dialogs
from tkinter.filedialog import *
from PyEditorCanvas import *
from PyExecutorFactory import *

class PyExecuteWnd(Tk):
    #初始化
    def __init__(self, title, parent=None):
        Tk.__init__(self, parent)
        self.factory = PyExecutorFactory().elementFactory()
        self.title(title)
        self.canvas=PyEditorCanvas(self, self.factory)
        self.makemenu()
        self.makeToolbar()
    
    #构建菜单
    def makemenu(self):
        top = Menu(self)
        self.config(menu=top) # set its menu option

        file = Menu(top, tearoff=False)
        file.add_command(label='Open', command=self.Load, underline=0)
        file.add_command(label='Save', command=self.Save, underline=0)
        file.add_command(label='Quit', command=self.quit, underline=0)
        top.add_cascade(label='File', menu=file, underline=0)

        #添加图形要素菜单
        add = Menu(top, tearoff=False)
        self.canvas.makemenu(add)
        top.add_cascade(label='Add', menu=add, underline=0)

    def makeToolbar(self):
        toolbar = Frame(self, relief=SUNKEN, bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        self.canvas.makeToolbar(toolbar)

    def Save(self):
        fn = asksaveasfile(mode='w', filetypes=(("JSON files", "*.json"),("PyExecutor configure data", '*.'+str(sys.argv[1]))),defaultextension='json')
        if fn:
            f = open(fn.name, 'w', encoding='utf-8')
            dict = {}
            dict['tag_factory'] = ExTagFactory().serialize()
            dict['canvas'] = self.canvas.serialize()
            json.dump(dict, f, cls=self.factory.jsonEncoder(), indent=4)
            f.close()

    def Load(self):
        file_name = askopenfilename(filetypes=(("PyExecutor files", "*.pye"),("All files", "*.*")))
