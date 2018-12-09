import sys
import tkinter
from ExFramework.ExTreeAccessor import *
from ExFramework.ExObserver import *
from ExFramework.ExBlock import *
from ExFramework.ExDiagram import *
from ExFramework.ExCustomBlock import *
from ExFramework.ExComponentDict import *

class PyExecutorTreeAccessor(ExTreeAccessor, ExObserver):
    def __init__(self, main_wnd):
        ExTreeAccessor.__init__(self)
        self.wnd = main_wnd
        self.__tree__ = None
        self.__blk_image__ = PhotoImage(file='images\\block.gif')
        self.__diagram_image__ = PhotoImage(file='images\\diagram.gif')

    def get_root(self):
        return self.wnd.top_diagram;

    def get_parent(self, node):
        return node.parent()

    def get_children(self, node):
        children = []
        if isinstance(node, ExDiagram):
            for c in node.children():
                if isinstance(c, ExBlock):
                    children.append(c)
        elif isinstance(node, ExCustomBlock):
            children.append(node.diagram())
        return children

    def get_name(self, node):
        return node.name()

    def get_iid(self, node):
        return node.tag()

    def get_image(self, node):
        if isinstance(node, ExDiagram):
            return self.__diagram_image__
        else:
            return self.__blk_image__

    def focus(self, iid):
        component = ExComponentDict().component(iid)
        if isinstance(component, ExDiagram):
            self.wnd.canvas.set_diagram(component)

    def update(self, component, ext):
        if isinstance(component, ExBlock):
            self.notify(component, ext)





