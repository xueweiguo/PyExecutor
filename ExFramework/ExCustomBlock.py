from ExFramework.ExBlock import *
from ExFramework.ExDiagram import *


class ExCustomBlock(ExBlock):
    def __init__(self, parent, name):
        ExBlock.__init__(self, parent, name, '用户自定义功能')

    def construct(self):
        ExBlock.construct(self)
        self.__diagram__ = ExDiagram(self, 'Sub Diagram').construct()
        return self

    def diagram(self):
        return self.__diagram__

    def append_input(self, name):
         ExInputPort(self, name, '输入'+name).construct()

    def append_output(self, name):
         ExOutputPort(self, name,'输出'+name).construct()

    # 生成属性对话框
    def create_property_dlg(self):
        return ExBlock.create_property_dlg(self)

    # 生成弹出菜单
    def create_popup(self, handler):
        menu = Menu(self.canvas, tearoff=False)
        menu.add_command(label='Property', command=(lambda: handler.on_command('Set Property')))
        menu.add_command(label='Delete', command=(lambda: handler.on_command('Delete')))
        return menu