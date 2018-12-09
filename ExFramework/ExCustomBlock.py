from ExFramework.ExBlock import *


class ExCustomBlock(ExBlock):
    def __init__(self, name):
        ExBlock.__init__(self, name, '用户自定义功能')

        # 生成属性对话框
        def create_property_dlg(self):
            return ExCustomPropertyDlg(self)

        # 生成弹出菜单
        def create_popup(self, handler):
            menu = Menu(self.canvas, tearoff=False)
            menu.add_command(label='Property', command=(lambda: handler.on_command('Set Property')))
            menu.add_command(label='Delete', command=(lambda: handler.on_command('Delete')))
            return menu