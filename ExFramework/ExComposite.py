from ExFramework.ExComponent import *

class ExComposite(ExComponent):
    def __init__(self, parent, name, comment):
        ExComponent.__init__(self, parent, name, comment)
        self.__children = []

    def construct(self):
        return ExComponent.construct(self)

    #添加子要素
    def append(self, child):
        self.__children.append(child)
        self.handle_request(child, 'append')

    #移除子要素
    def remove(self, child):
        self.handle_request(child, 'remove')
        self.__children.remove(child)

    #@canvas.setter
    def attach_canvas(self, canvas):
        ExComponent.attach_canvas(self, canvas)
        for c in self.children():
            c.canvas = canvas

    def detach_canvas(self):
        for c in self.children():
            c.canvas = None
        ExComponent.detach_canvas(self)

    #系列化要素
    def serialize(self):
        return ExComponent.serialize(self)
        for c in self.children():
            c.serialize()

    #取得子节点列表
    def children(self):
        return self.__children

    def countChild(self, child_class):
        count = 0
        for child in self.children():
            if isinstance(child, child_class):
                count = count + 1
        return count

    def findChild(self, name):
        for child in self.children():
            if child.name == name:
                return child
        return None



