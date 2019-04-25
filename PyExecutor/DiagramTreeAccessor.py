import sys
import os

import tkinter
from Foundation.TreeAccessor import *
from Framework.CustomBlock import *


class DiagramTreeAccessor(TreeAccessor):
    def __init__(self, wnd):
        TreeAccessor.__init__(self)
        self.wnd = wnd
        cur_path = os.path.abspath(os.path.dirname(__file__))
        self.__blk_image = PhotoImage(file=cur_path + '\\images\\block.gif')
        self.__diagram_image = PhotoImage(file=cur_path + '\\images\\diagram.gif')

    def get_parent(self, node):
        return node.parent

    # 取得节点名称
    def get_name(self, node):
        return node.name

    # 取得节点图标
    def get_image(self, node):
        # 根据节点类型返回图标
        if isinstance(node, Diagram):
            return self.__diagram_image
        else:
            return self.__blk_image

    # 取得节点iid
    def get_iid(self, node):
        # 返回Component的tag
        return node.tag

    # 取得下级节点
    def get_children(self, node):
        return node.iter('tree_node')

    def focus(self, iid):
        component = self.wnd.view.dict[iid]
        if isinstance(component, Diagram):
            self.wnd.focus_diagram(component)







