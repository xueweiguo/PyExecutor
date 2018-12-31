from ExFramework.ExObserver import *
from ExFramework.ExTreeView import *
from ExFramework.ExBlock import *

class PyDiagramObserver(ExObserver):
    def __init__(self, tree_view):
        self.tree = tree_view

    # ExObserver.update()
    def update(self, component, ext):
        if isinstance(component, ExBlock):
            if ext == 'append':
                self.tree.append_node(component)
            elif ext == 'remove':
                self.tree.remove_node(component)