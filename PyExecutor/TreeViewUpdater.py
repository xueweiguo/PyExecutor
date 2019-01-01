from ExFramework.ExObserver import *
from ExFramework.ExTreeView import *
from ExFramework.ExBlock import *


# 根据接收到的TopDigram的通知，更新TreeView的内容
class TreeViewUpdater(ExObserver):
    def __init__(self, tree_view):
        self.tree = tree_view

    # ExObserver.update()
    def update(self, component, ext):
        if isinstance(component, ExBlock):
            if ext == 'append':
                self.tree.append_node(component)
            elif ext == 'remove':
                self.tree.remove_node(component)
