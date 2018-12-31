import sys
import tkinter
from ExFramework.ExTreeAccessor import *
from ExFramework.ExBlock import *
from ExFramework.ExDiagram import *
from ExFramework.ExCustomBlock import *
from ExFramework.ExComponentDict import *


class PyExecutorTreeAccessor(ExTreeAccessor):
    def __init__(self, main_wnd):
        ExTreeAccessor.__init__(self)
        self.wnd = main_wnd
        self.__tree__ = None
        self.__blk_image__ = PhotoImage(file='images\\block.gif')
        self.__diagram_image__ = PhotoImage(file='images\\diagram.gif')

    def get_root(self):
        return self.wnd.top_diagram;

    def get_parent(self, node):
        return node.parent

    # 取得节点名称
    def get_name(self, node):
        return node.name

    # 取得节点图标
    def get_image(self, node):
        # 根据节点类型返回图标
        if isinstance(node, ExDiagram):
            return self.__diagram_image__
        else:
            return self.__blk_image__

    # 取得节点iid
    def get_iid(self, node):
        # 返回ExComponent的tag
        return node.tag

    # 取得下级节点
    def get_children(self, node):
        children = []
        # 如果时ExDiagram对象，返回下级ExBlock节点
        if isinstance(node, ExDiagram):
            for c in node.children():
                if isinstance(c, ExBlock):
                    children.append(c)
        # 如果时ExCustomBlock对象，返回内部的ExDiagram
        elif isinstance(node, ExCustomBlock):
            children.append(node.diagram())
        else:
            # 其他类型节点，表示对象外。
            pass
        return children

    def focus(self, iid):
        component = ExComponentDict().component(iid)
        if isinstance(component, ExDiagram):
            self.wnd.canvas.diagram = component







