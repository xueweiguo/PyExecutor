from Foundation.Iterators import *
from Framework.Component import *


class Composite(Component):
    def __init__(self, cd, name, comment):
        Component.__init__(self, cd, name, comment)
        self.__children = []

    def construct(self, parent):
        return Component.construct(self, parent)

    def destruct(self):
        # print(self, 'Composite.destruct')
        for child in self.iter():
            child.destruct()
        Component.destruct(self)

    def copy(self, memo):
        c = Component.copy(self, memo)
        c.__children = []
        for child in self.iter():
            c.append(child.copy(memo))
        return c

    def accept(self, visitor, mode='DLR'):
        if mode=='DLR':
            Component.accept(self, visitor, mode)
        for c in self.iter():
            c.accept(visitor, mode)
        if mode=='LRD':
            Component.accept(self, visitor, mode)

    #添加子要素
    def append(self, child):
        self.__children.append(child.tag)
        child.set_parent(self)
        self.handle_request(child, 'append')

    # 插入子要素
    def insert(self, child, index):
        self.__children.insert(index, child.tag)
        if self.canvas:
            child.attach_view(self.view)
        self.handle_request(child, 'insert', {'parent': self, 'index': index})

    #移除子要素
    def remove(self, child):
        child.detach_view()
        index = self.__children.index(child.tag)
        self.__children.remove(child.tag)
        self.handle_request(child, 'remove', {'index': index})

    def attach_view(self, view):
        Component.attach_view(self, view)
        for c in self.iter():
            c.attach_view(view)

    def detach_view(self):
        for c in self.iter():
            c.detach_view()
        Component.detach_view(self)

    # 取得子节点迭代器
    def iter(self, mode=''):
        if self.dict:
            return map(self.dict.__getitem__, self.__children)
        else:
            return iter([])

    def count_child(self, child_class):
        counter = 0
        for child in type_filter(self.iter(), child_class):
            counter = counter + 1
        return counter

    def find_child(self, tag):
        for child in self.iter():
            if child.tag == tag:
                return child
        return None
