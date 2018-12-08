from ExFramework.ExTreeAccessor import *
from ExFramework.ExObserver import *
from ExFramework.ExBlock import *
class ExDiagramTreeAccessor(ExTreeAccessor, ExObserver):
    def __init__(self, diagram):
        ExTreeAccessor.__init__(self)
        self.__diagram__ = diagram
        self.__tree__ = None

    def get_root(self):
        return self.__diagram__;

    def get_parent(self, node):
        return node.parent()

    def get_children(self, node):
        children = []
        for c in node.children():
            if isinstance(c, ExBlock):
                children.append(c)
        return children

    def get_name(self, node):
        return node.name()

    def get_iid(self, node):
        return node.tag()

    def update(self, component, ext):
        if isinstance(component, ExBlock):
            self.notify(component, ext)





