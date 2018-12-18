from ExFramework.ExElement import *
from ExFramework.ExTagFactory import *
from ExFramework.ExNotePropertyDlg import *

#信息标签
class ExNote(ExElement):
    def __init__(self, parent):
        ExComponent.__init__(self, parent, '', '信息标签')

    def construct(self):
        ExComponent.construct(self)
        self.tag = self.handle_request(self, 'create_tag')
        return self

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def attach_canvas(self, canvas):
        self._canvas = canvas
        self._frame = canvas.create_rectangle(self.x, self.y, self.x + 100, self.y + 60, fill='lightyellow', tag=self.tag)
        ExElement.attach_canvas(self, canvas)


    def set_color(self, color):
        self._canvas.itemconfigure(self._frame, outline=color)

    def move(self, x, y):
        self._canvas.move(self.tag, x, y)
        self.x = self.x + x
        self.y = self.y + y

    # 生成属性对话框
    def create_property_dlg(self):
        return ExNotePropertyDlg(self)

    # 生成弹出菜单
    def create_popup(self, handler):
        menu = Menu(self._canvas, tearoff=False)
        menu.add_command(label='Property', command=(lambda: handler.on_command('SetProperty')))
        menu.add_command(label='Delete', command=(lambda: handler.on_command('Delete')))
        return menu