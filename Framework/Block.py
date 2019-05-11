from tkinter import *
from Foundation.Iterators import *
from Framework.Composite import *
from Framework.InputPort import *
from Framework.OutputPort import *
from Framework.PropertyDlg import *
from Framework.BlockTab import *
from Framework.CommonTab import *
from Framework.EditCommand import *


class blk_memento:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.c_memento = {}


# 功能模块
class Block(Composite):
    def __init__(self, cd, name, comment):
        Composite.__init__(self, cd, name, comment)
        self._caption_height = 20
        self.top_offset = 0
        self.x = None
        self.y = None
        self.width = 80
        self.bottom_margin = 0.5
        self.last_pos = 0

    def iter(self, mode=''):
        if mode == 'tree_node':
            return iter([])
        elif mode=='input_port':
            return type_filter(Composite.iter(self), InputPort)
        elif mode == 'output_port':
            return type_filter(Composite.iter(self), OutputPort)
        else:
            return Composite.iter(self, mode)

    # 添加子要素
    def append(self, child):
        if isinstance(child, DataPort):
            if child.pos > self.last_pos:
                self.last_pos = child.pos
        Composite.append(self, child)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x,self.y

    def get_x(self):
        return self.x

    def resize(self):
        self.last_pos = 0
        for port in self.iter():
            port.relocation()
        self.canvas.coords(self.__frame, self.left, self.top, self.right, self.bottom)

    def set_color(self, color):
        self.canvas.itemconfigure(self.__frame, outline=color)

    # 挂接Canvas
    def attach_view(self, view):
        view.canvas.create_rectangle(self.left, self.top, self.right, self.bottom,
                                     tags=[self.tag, self.__frame], fill='white', outline='black')
        view.canvas.create_text(self.left + 40, self.top, tags=[self.tag, self.__caption], text=self.name, anchor=N)
        # 调用父类功能
        Composite.attach_view(self, view)

    # 脱离Canvas
    def detach_view(self):
        self.canvas.delete(self.__frame)
        self.canvas.delete(self.__caption)
        # 调用父类功能
        Composite.detach_view(self)

    def create_memento(self):
        memento = blk_memento(self.x, self.y)
        for port in self.iter('input_port'):
            connector = port.connector
            if connector:
                memento.c_memento[connector.tag] = connector.create_memento()

        for port in self.iter('output_port'):
            for i in range(0, port.c_count()):
                connector = port.connector(i)
                memento.c_memento[connector.tag] = connector.create_memento()
        return memento

    def set_memento(self, memento):
        self.move(memento.x - self.x, memento.y - self.y)
        for tag, c_m in memento.c_memento.items():
            self.dict[tag].set_memento(c_m)

    def accept(self, visitor, mode='DLR'):
        ok = True
        if mode=='DLR':
            ok = visitor.visit_block(self)
        if ok:
            for in_port in self.iter('input_port'):
                in_port.accept(visitor, mode)
            visitor.visit_body(self)
            for out_port in self.iter('output_port'):
                out_port.accept(visitor, mode)
        if mode=='LRD':
            visitor.visit_block(self)

    def reset_connections(self, memo):
        pass

    def move(self, x, y):
        if self.canvas:
            self.canvas.move(self.tag, x, y)
        for port in self.iter():
            port.on_move()
        self.x = self.x + x
        self.y = self.y + y
        self.resize()
        self.handle_request(self, 'block_move')

    def caption_height(self):
        return self._caption_height

    @property
    def left(self):
        return self.x

    @property
    def top(self):
        return self.y + self.top_offset

    @property
    def right(self):
        return self.x + self.width

    @property
    def bottom(self):
        # 计算功能模块高度
        height = self._caption_height + (self.last_pos + 1) * DataPort.height()
        height = height + self.bottom_margin * DataPort.height()
        return self.top + height

    def port(self, name):
        for child in self.iter():
            if child.name == name:
                return child
        return None

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = PropertyDlg(self)
        dlg.add_tab(CommonTab(dlg.notebook(), '共通', self))
        dlg.add_tab(BlockTab(dlg.notebook(), '参数', self))
        return dlg

    # 生成弹出菜单
    def create_popup(self, handler):
        menu = Menu(self.canvas, tearoff=False)
        menu.add_command(label='Property',
                         command=(lambda: handler.on_command('SetProperty')))
        menu.add_command(label='Copy',
                         command=(lambda: handler.on_command('Copy')))
        menu.add_command(label='Delete',
                         command=(lambda: handler.on_command('Delete')))

        return menu

    def name_changed(self):
        try:
            self.canvas.itemconfigure(self.__caption, text=self.name)
            self.handle_request(self, 'change_name')
        except:
            pass  # do nothing

    @property
    def __caption(self):
        return self.tag + '.caption'

    @property
    def __frame(self):
        return self.tag + '.frame'

    def start(self, context):
        pass

    def stop(self, context):
        pass

    def execute(self, context):
        pass







