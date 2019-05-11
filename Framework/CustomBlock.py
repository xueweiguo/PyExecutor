from Framework.Block import *
from Framework.CustomBlockTab import *
from Framework.Diagram import *


class CustomBlock(Block):
    def __init__(self, cd=None, name=''):
        Block.__init__(self, cd, name, '用户自定义功能')
        self.__diagram = None

    def construct(self, parent):
        Block.construct(self, parent)
        diagram = Diagram(self.dict, 'Sub Diagram')
        diagram.construct(self)
        self.__diagram = diagram.tag
        return self

    def copy(self, memo):
        c = Block.copy(self, memo)
        diagram = self.diagram().copy(memo)
        diagram.set_parent(c)
        c.__diagram = diagram.tag
        memo[self.__diagram] = c.__diagram
        return c

    def accept(self, visitor, mode='DLR'):
        if mode=='DLR':
            Block.accept(self, visitor, mode)
        self.diagram().accept(visitor, mode)
        if mode=='LRD':
            Block.accept(self, visitor, mode)

    def diagram(self):
        return self.dict[self.__diagram]

    def iter(self, mode=''):
        if mode == 'tree_node':
            return iter([self.diagram()])
        else:
            return Block.iter(self, mode)

    def append_input(self, pos, name, comment):
         InputPort(self.dict, pos, name, comment).construct(self)

    def append_output(self, pos, name, comment):
         OutputPort(self.dict, pos, name, comment).construct(self)

    # 添加子要素
    def append(self, child):
        Block.append(self, child)
        if self.canvas:
            self.resize()

    # 插入子要素
    def insert(self, child, index):
        Block.insert(child, index)
        self.resize()

    # 移除子要素
    def remove(self, child):
        Block.remove(self, child)
        self.resize()

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = PropertyDlg(self)
        dlg.add_tab(CommonTab(dlg.notebook(), '共通', self))
        dlg.add_tab(CustomBlockTab(dlg.notebook(), '参数', self))
        return dlg






