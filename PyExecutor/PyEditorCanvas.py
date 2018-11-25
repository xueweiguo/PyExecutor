import sys

sys.path.append('..')
from ExFramework.ScrollCanvas import *
from PyCanvasStateMachine import *
from ExFramework.ExTagFactory import *

class PyEditorCanvas(ScrollCanvas):
    def __init__(self, parent, factory, color='lightyellow'):
        ScrollCanvas.__init__(self, parent, color)
        self.factory = factory
        self.element_type = None
        self.drawn = None
        self.start = None
        self.active = None
        self.connector = None
        self.__element_dict = {}
        self.machine = PyCanvasStateMachine(self)
        self.machine.entry()

    # 构建工具条
    def makeToolbar(self, toolbar):
        types = self.factory.element_types()
        for i in range(len(types)):
            Button(toolbar, text=types[i], command=(lambda index=i: self.addElement(index))).pack(side=LEFT)

    # 构建菜单项
    def makemenu(self, menu):
        # 功能块子菜单
        types = self.factory.element_types()
        for i in range(len(types)):
            menu.add_command(label=types[i], command=(lambda index=i: self.addElement(index)))


    # 构建功能块
    def addElement(self, index):
        types = self.factory.element_types()
        self.element_type = types[index]
        self.canvas.configure(cursor='dotbox')

    #
    def register_element(self, element):
        tag = ExTagFactory().createTag()
        element.set_tag(tag)
        self.__element_dict[tag] = element

    def remove_element(self, element):
        tag = element.tag()
        self.canvas.delete(tag)
        self.__element_dict.pop(tag)

    # 根据tags查找要素
    def find_element(self, tags):
        tag_count = len(tags)
        if tag_count > 0:
            if tags[tag_count - 1] == 'current':
                tag_count = tag_count - 1
            if tag_count > 0:
                element = self.__element_dict[tags[0]]
                if element != None:
                    if tag_count > 1:
                        return element.findChild(tags[1])
                    else:
                        return element
        return None

        # 根据坐标查找要素

    def find_overlapping(self, x, y):
        ids = self.canvas.find_overlapping(x, y, x + 1, y + 1)
        if len(ids) > 0:
            tags = self.canvas.gettags(ids[0])
            if len(tags) > 0:
                return self.find_element(tags)
        return None

    # 删除选中的要素
    def deleteCurrent(self):
        pass

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
        for key in self.__element_dict:
            list.append(self.__element_dict[key].serialize())
        return list

    def grid(self, event):
        half = 2
        event.x = self.canvas.canvasx(event.x)
        event.x = int((event.x + half) / (half * 2)) * (half * 2)
        event.y = self.canvas.canvasy(event.y)
        event.y = int((event.y + half) / (half * 2)) * (half * 2)
        return event

