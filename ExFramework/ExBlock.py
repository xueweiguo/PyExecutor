from tkinter import *
from ExFramework.ExElement import *
from ExFramework.ExInputPort import *
from ExFramework.ExOutputPort import *
from ExFramework.ExBlockTab import *

#功能块
class ExBlock(ExElement):
    def __init__(self, parent, name, comment):
        ExElement.__init__(self, parent, name, comment)
        self._frame = None
        self._caption = None

    def construct(self):
        self.set_tag(self.handle_request(self, 'create_tag'))
        return self

    def set_position(self, x, y):
        self.x = x
        self.y = y

    #挂接canvas
    def attach_canvas(self, canvas):
        self._frame = canvas.create_rectangle(self.left(), self.top(), self.right(), self.bottom(),
                                              tag=self.tag(), fill='white', outline='black')
        self.caption = canvas.create_text(self.x + 40, self.y, tag=self.tag(), text=self.name(), anchor=N)
        #调用父类功能
        ExElement.attach_canvas(self, canvas)

    #脱离canvas
    def detach_canvas(self):
        self._canvas.delete(self._frame)
        self._frame = None
        if self.caption:
            self._canvas.delete(self.caption)
            self.caption = None
        ExElement.detach_canvas(self)

    def move(self, x, y):
        self._canvas.move(self.tag(), x, y)
        for port in self.children():
            port.move()
        self.x = self.x + x
        self.y = self.y + y

    def port_start(self):
        return self.top() + 20

    def left(self):
        return self.x

    def top(self):
        return self.y

    def right(self):
        return self.x + 80

    def bottom(self):
        # 计算功能模块高度
        docking_count = max(self.countChild(ExInputPort), self.countChild(ExOutputPort))
        return self.port_start() + docking_count * ExPort.height()

    def set_color(self, color):
        self._canvas.itemconfigure(self._frame, outline=color)

    def serialize(self):
        coords = self._canvas.coords(self._frame)
        dict = ExElement.serialize(self)
        dict.update({'x':coords[0], 'y':coords[1]})
        port_list = []
        for port in self.children():
            port_list.append(port.serialize())
        dict['ports'] = port_list
        return dict

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = ExElement.create_property_dlg(self)
        dlg.add_tab(ExBlockTab(dlg.notebook(), '参数', self))
        return dlg

    # 生成弹出菜单
    def create_popup(self, handler):
        menu = Menu(self._canvas, tearoff=False)
        menu.add_command(label='Property', command=(lambda: handler.on_command('SetProperty')))
        menu.add_command(label='Delete', command=(lambda: handler.on_command('Delete')))
        return menu


