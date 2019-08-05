from Foundation.Iterators import *
from Framework.Composite import *
from Framework.TagFactory import *
from Framework.InputBlock import *
from Framework.OutputBlock import *
from Framework.Connector import *
from Framework.InputPortFinder import *


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
            child.attach_view(self.view)
        # print(self)

    def remove(self, child):
        # 如果删除对象是Block
        if isinstance(child, Block):
            self.handle_request(child, 'begin_macro')
            # 遍历所有输入端口，删除输入连接线
            for port in child.iter('input_port'):
                if port.connector:
                    c = port.connector
                    c.disconnect()
                    Composite.remove(self, c)
            # 遍历所有出端口，删除所有输出连接线
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
        # print(self)

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

    def find_in_port(self, x, y):
        #for block in reversed(type_filter(self.iter(), Block)):
        try:
            blocks = list(type_filter(self.iter(), Block))
            for block in reversed(blocks):
                finder = InputPortFinder(x, y)
                block.accept(finder)
                if finder.in_port:
                    return finder.in_port
            return None
        except Exception as e:
            print('Error:', e, '.')
            return None


    @property
    def uc(self):
        if self.view:
            return self.view.undo_controller(self.tag)
        else:
            return None

    def redo(self):
        self.uc.redo()
        # print(self)

    def redone(self):
         return self.uc.redone()

    def undo(self):
        self.uc.undo()
        # print(self)

    def undone(self):
        return self.uc.undone()

    # 请求处理
    def handle_request(self, component, req, params=None):
        # 记录操作请求，用于撤销和重做处理
        if self.uc:
            self.uc.handle_request(component, req, params)
        # 请求转发
        ret = Composite.handle_request(self, component, req, params)
        # 如果Diagram正好被DiagramView表示，则调用DiagramView的Observable接口
        if self.view:
            self.view.notify(component, req, params)
        return ret

    def __str__(self):
        str = '<Diagram>\n'
        for c in self.iter(self):
            str += c.__str__() + '\n'
        return str

