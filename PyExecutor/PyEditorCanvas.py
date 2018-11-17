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
        self.active = None
        self.connector = None
        self.element_dict = {}
        self.tag = 1
        self.machine = PyCanvasStateMachine(self)
        self.machine.entry()

    #根据tags查找要素
    def find_element(self, tags):
        tag_count = len(tags)
        if tag_count > 0:
            if tags[tag_count-1] == 'current':
                tag_count = tag_count-1
            if tag_count > 0:
                element = self.element_dict[tags[0]]
                if element != None:
                    if tag_count > 1:
                        return element.findChild(tags[1])
                    else:
                        return element
        return None

    #根据坐标查找要素
    def find_overlapping(self, x, y):
        ids = self.canvas.find_overlapping(x, y, x + 1, y + 1)
        if len(ids) > 0:
            tags = self.canvas.gettags(ids[0])
            if len(tags) > 0:
                return self.find_element(tags)
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

    # 删除选中的要素
    def deleteCurrent(self):
        pass

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
        self.machine.eventHandling('LButtonDoubleClick', self.grid(event))

    def onLButtonDown(self, event):
        self.machine.eventHandling('LButtonDown',  self.grid(event))

    def onRButtonDown(self, event):
        self.machine.eventHandling('RButtonDown',  self.grid(event))

    def onLButtonMove(self, event):
        self.machine.eventHandling('LButtonMove',  self.grid(event))

    def onMouseMove(self, event):
        self.machine.eventHandling('MouseMove',  self.grid(event))

    def onLButtonUp(self, event):
        self.machine.eventHandling('LButtonUp',  self.grid(event))

    def onKey(self, event):
        self.machine.eventHandling('Key',  self.grid(event))

    def set_active(self, act):
        if self.active != act:
            if self.active:
                self.active.set_color('black')
                self.active = None
            if act:
                act.set_color('red')
                self.active = act

    def serialize(self):
        list = []
        for key in self.element_dict:
            list.append(self.element_dict[key].serialize())
        return list

    def grid(self, event):
        half = 2
        event.x = self.canvas.canvasx(event.x)
        event.x = int((event.x + half) / (half * 2)) * (half * 2)
        event.y = self.canvas.canvasy(event.y)
        event.y = int((event.y + half) / (half * 2)) * (half * 2)
        return event

