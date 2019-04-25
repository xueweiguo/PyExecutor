from Foundation.Iterators import *
from Framework.Composite import *
from Framework.TagFactory import *
from Framework.InputBlock import *
from Framework.OutputBlock import *
from Framework.Connector import *


class Diagram(Composite):
    def __init__(self, cd=None, name='', comment=''):
        Composite.__init__(self, cd, name, comment)

    def construct(self, parent):
        Composite.construct(self, parent)
        self.tag = self.dict.create_tag()
        self.dict.register(self)
        return self

     # 添加子要素
    def append(self, child):
        Composite.append(self, child)
        if self.canvas:
            child.attach_canvas(self.canvas)

    def remove(self, child):
        if isinstance(child, Block):
            self.handle_request(child, 'begin_macro')
            for port in child.iter('input_port'):
                if port.connector:
                    c = port.connector
                    c.disconnect()
                    Composite.remove(self, c)

            for port in child.iter('output_port'):
                for i in range(0, port.c_count()):
                    c = port.connector(i)
                    c.disconnect()
                    Composite.remove(self, c)
            Composite.remove(self, child)
            self.handle_request(child, 'end_macro')
        elif isinstance(child, Connector):
            self.handle_request(child, 'begin_macro')
            child.disconnect()
            Composite.remove(self, child)
            self.handle_request(child, 'end_macro')
        else:
            Composite.remove(self, child)

    def iter(self, mode=''):
        if mode == 'tree_node':
            return type_filter(Composite.iter(self), Block)
        else:
            return Composite.iter(self)

    def accept(self, visitor, mode='DLR'):
        if mode=='DLR':
            Component.accept(self, visitor, mode)
            visitor.visit_diagram(self)
        children = []
        for b in Composite.iter(self):
            children.append(b)
        children.sort(key=Block.get_x)
        for b in children:
            b.accept(visitor, mode)
        if mode=='LRD':
            Component.accept(self, visitor)
            visitor.visit_diagram(self)

    @property
    def observable(self):
        if self.canvas:
            return self.canvas.observable()
        else:
            return None

    @property
    def uc(self):
        if self.canvas:
            return self.canvas.undo_controller(self.tag)
        else:
            return None

    def redo(self):
        self.uc.redo()

    def redone(self):
         return self.uc.redone()

    def undo(self):
        self.uc.undo()

    def undone(self):
        return self.uc.undone()

    # 请求处理
    def handle_request(self, component, req, params=None):
        if self.uc:
            self.uc.handle_request(component, req, params)
        ret = Composite.handle_request(self, component, req, params)
        if self.observable:
            self.observable.notify(component, req, params)
        return ret
