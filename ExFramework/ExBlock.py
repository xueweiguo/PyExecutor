from tkinter import *
from ExFramework.ExElement import *
from ExFramework.ExInputPort import *
from ExFramework.ExOutputPort import *
from ExFramework.ExBlockTab import *

#功能块
class ExBlock(ExElement):
    def __init__(self, parent, name, comment):
        ExElement.__init__(self, parent, name, comment)
        self.frame = None
        self.caption = None

    def construct(self):
        self.set_tag(self.handle_request(self, 'create_tag'))
        return self

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def attach_canvas(self, canvas):
        self.canvas= canvas
        blk_width = 80
        port_start = 20
        port_height = 10
        blk_height = port_start + max(self.countChild(ExInputPort), self.countChild(ExOutputPort)) * port_height
        self.frame = canvas.create_rectangle(self.x, self.y, self.x+blk_width, self.y+blk_height, tag=self.tag(),
                                             fill='white', outline='black')
        self.caption = canvas.create_text(self.x + 40, self.y, tag=self.tag(), text=self.name(), anchor=N)

        port_y = self.y + port_start
        for port in self.children():
            if isinstance(port, ExInputPort):
                port.set_position(self.x, port_y)
                port.attach_canvas(canvas)
                port_y = port_y + port_height

        port_y = self.y + port_start
        for port in self.children():
            if isinstance(port, ExOutputPort):
                port.set_position(self.x + blk_width, port_y)
                port.attach_canvas(canvas)
                port_y = port_y + port_height

    def detach_canvas(self):
        self.canvas.delete(self.frame)
        self.frame = None
        if self.caption:
            self.canvas.delete(self.caption)
            self.caption = None
        ExElement.detach_canvas(self)

    def move(self, x, y):
        self.canvas.move(self.tag(), x, y)
        for port in self.children():
            port.on_move()
        self.x = self.x + x
        self.y = self.y + y

    def set_color(self, color):
        self.canvas.itemconfigure(self.frame, outline=color)

    def serialize(self):
        coords = self.canvas.coords(self.frame)
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
        menu = Menu(self.canvas, tearoff=False)
        menu.add_command(label='Property', command=(lambda: handler.on_command('SetProperty')))
        menu.add_command(label='Delete', command=(lambda: handler.on_command('Delete')))
        return menu


