from ExFramework.ExElement import *
from ExFramework.ExTagFactory import *
from ExFramework.ExNotePropertyDlg import *

#信息标签
class ExNote(ExElement):
    def __init__(self):
        ExComponent.__init__(self, '', '信息标签')

    def attach(self, canvas, x, y):
        self.canvas = canvas
        self.frame = canvas.create_rectangle(x, y, x + 100, y + 60, fill='lightyellow', tag=self.tag())

    def set_color(self, color):
        self.canvas.itemconfigure(self.frame, outline=color)

    # 生成属性对话框
    def create_property_dlg(self):
        return ExNotePropertyDlg(self)

    # 生成弹出菜单
    def create_popup(self, handler):
        menu = Menu(self.canvas, tearoff=False)
        menu.add_command(label='Property', command=(lambda: handler.on_command('SetProperty')))
        menu.add_command(label='Delete', command=(lambda: handler.on_command('Delete')))
        return menu