from ExFramework.ExBlock import *
from ExFramework.ExDiagram import *


class ExCustomBlock(ExBlock):
    def __init__(self, name):
        ExBlock.__init__(self, name, '用户自定义功能')
        self.__diagram__ = ExDiagram('Sub Diagram')
        self.__diagram__.set_parent(self)

    def diagram(self):
        return self.__diagram__

    def append_input(self, name):
        self.append(ExInputPort(name, '输入'+name, self))

    def append_output(self, name):
         self.append(ExOutputPort(name,'输出'+name, self))

    # 生成属性对话框
    def create_property_dlg(self):
        return ExBlock.create_property_dlg(self)

    # 生成弹出菜单
    def create_popup(self, handler):
        menu = Menu(self.canvas, tearoff=False)
        menu.add_command(label='Property', command=(lambda: handler.on_command('Set Property')))
        menu.add_command(label='Delete', command=(lambda: handler.on_command('Delete')))
        return menu