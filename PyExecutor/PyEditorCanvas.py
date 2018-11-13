from tkinter import * # get widget classes
from tkinter.messagebox import * # get standard dialogs

import sys
import json
sys.path.append('..')
from ExFramework.ExComponentFactory import *
from ExFramework.ScrollCanvas import *
from ExFramework.ExTagFactory import *
from PyCanvasStateMachine import *

class PyEditorCanvas(ScrollCanvas):
    def __init__(self, parent, factory, color='lightyellow'):
        ScrollCanvas.__init__(self, parent, color)
        self.factory = factory
        self.element_type = None
        self.drawn = None
        self.start = None
        self.connector = None
        self.element_dict = {}
        self.tag = 1
        self.machine = PyCanvasStateMachine(self)
        self.machine.entry()

    #根据tags查找要素
    def findComponent(self, tags):
        if len(tags) > 0:
            element = self.element_dict[tags[0]]
            if element == None:
                return None
            elif len(tags) > 1:
                return element.findChild(tags[1])
            else:
                return element
        else:
            return None


    # 构建工具条
    def makeToolbar(self, toolbar):
        types = self.factory.elementTypes()
        Button(toolbar, text='Initial', command=self.addInitial).pack(side=LEFT)
        Button(toolbar, text='Final', command=self.addFinal).pack(side=LEFT)
        item_count = len(types)
        if item_count > 0:
            Button(toolbar, text=types[0], command=(lambda: self.addElement(0))).pack(side=LEFT)
        if item_count > 1:
            Button(toolbar, text=types[1], command=(lambda: self.addElement(1))).pack(side=LEFT)
        if item_count > 2:
            Button(toolbar, text=types[2], command=(lambda: self.addElement(2))).pack(side=LEFT)
        if item_count > 3:
            Button(toolbar, text=types[3], command=(lambda: self.addElement(3))).pack(side=LEFT)
        if item_count > 4:
            Button(toolbar, text=types[4], command=(lambda: self.addElement(4))).pack(side=LEFT)
        if item_count > 5:
            Button(toolbar, text=types[5], command=(lambda: self.addElement(5))).pack(side=LEFT)
        if item_count > 6:
            Button(toolbar, text=types[6], command=(lambda: self.addElement(6))).pack(side=LEFT)
        if item_count > 7:
            Button(toolbar, text=types[3], command=(lambda: self.addElement(7))).pack(side=LEFT)
        if item_count > 8:
            Button(toolbar, text=types[4], command=(lambda: self.addElement(8))).pack(side=LEFT)
        if item_count > 9:
            Button(toolbar, text=types[5], command=(lambda: self.addElement(9))).pack(side=LEFT)
        if item_count > 10:
            Button(toolbar, text=types[6], command=(lambda: self.addElement(10))).pack(side=LEFT)


    # 构建菜单项
    def makemenu(self, menu):
        menu.add_command(label='Initial', command=self.addInitial)
        menu.add_command(label='Final', command=self.addFinal)

        # 功能块子菜单
        submenu = Menu(menu, tearoff=False)
        types = self.factory.elementTypes()
        item_count = len(types)
        if item_count > 0:
            submenu.add_command(label=types[0], command=(lambda: self.addElement(0)))
        if item_count > 1:
            submenu.add_command(label=types[1], command=(lambda: self.addElement(1)))
        if item_count > 2:
            submenu.add_command(label=types[2], command=(lambda: self.addElement(2)))
        if item_count > 3:
            submenu.add_command(label=types[3], command=(lambda: self.addElement(3)))
        if item_count > 4:
            submenu.add_command(label=types[4], command=(lambda: self.addElement(4)))
        if item_count > 5:
            submenu.add_command(label=types[5], command=(lambda: self.addElement(5)))
        if item_count > 6:
            submenu.add_command(label=types[6], command=(lambda: self.addElement(6)))
        if item_count > 7:
            submenu.add_command(label=types[5], command=(lambda: self.addElement(7)))
        if item_count > 8:
            submenu.add_command(label=types[6], command=(lambda: self.addElement(8)))
        if item_count > 9:
            submenu.add_command(label=types[5], command=(lambda: self.addElement(9)))
        if item_count > 10:
            submenu.add_command(label=types[6], command=(lambda: self.addElement(10)))

        menu.add_cascade(label='Elements', menu=submenu)



    # 构建起始点
    def addInitial(self):
        self.element_type="Initial"
        self.canvas.configure(cursor='dot')

    # 构建终止点
    def addFinal(self):
        self.element_type="Final"
        self.canvas.configure(cursor='dot')

    # 构建功能块
    def addElement(self, index):
        types = self.factory.elementTypes()
        self.element_type=types[index]
        self.canvas.configure(cursor='dotbox')

    def onDoubleClick(self, event):
        event.x = self.canvas.canvasx(event.x)
        event.y = self.canvas.canvasy(event.y)
        self.machine.eventHandling('LButtonDoubleClick', event)

    def onLButtonDown(self, event):
        event.x = self.canvas.canvasx(event.x)
        event.y = self.canvas.canvasy(event.y)
        self.machine.eventHandling('LButtonDown', event)

    def onRButtonDown(self, event):
        event.x = self.canvas.canvasx(event.x)
        event.y = self.canvas.canvasy(event.y)
        self.machine.eventHandling('RButtonDown', event)

    def onLButtonMove(self, event):
        event.x = self.canvas.canvasx(event.x)
        event.y = self.canvas.canvasy(event.y)
        self.machine.eventHandling('LButtonMove', event)

    def onMouseMove(self, event):
        event.x = self.canvas.canvasx(event.x)
        event.y = self.canvas.canvasy(event.y)
        self.machine.eventHandling('MouseMove', event)

    def onLButtonUp(self, event):
        event.x = self.canvas.canvasx(event.x)
        event.y = self.canvas.canvasy(event.y)
        self.machine.eventHandling('LButtonUp', event)

    def serialize(self):
        list = []
        for key in self.element_dict:
            list.append(self.element_dict[key].serialize())
        return list
