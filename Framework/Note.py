from Framework.Component import *
from Framework.PropertyDlg import *
from Framework.CommonTab import *
from Framework.NoteTab import *


#信息标签
class Note(Component):
    def __init__(self, parent=None):
        Component.__init__(self, parent, 'Note', '信息标签')
        self.x = None
        self.y = None
        self.__note = '自由记述'

    def construct(self, parent):
        return Component.construct(parent)

    def copy(self, memo):
        c = Component.copy(self, memo)
        c.x = self.x
        c.y = self.y
        c.__note = self.__note
        return c

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def attach_view(self, view):
        Component.attach_view(self, view)
        self.canvas.create_text(self.x, self.y, anchor=SW,
                                tags=[self.tag, self.caption], text=self.name)
        self.canvas.create_rectangle(self.x, self.y, self.x + 100, self.y + 60,
                                     fill='lightyellow',
                                     tags=[self.tag, self.frame])
        self.canvas.create_text(self.x, self.y , anchor=NW,
                                tags=[self.tag, self.note_id], text=self.__note)
        Component.attach_view(self, view)

    def create_memento(self):
        return self.get_position()

    def set_memento(self, memento):
        self.move(memento.x - self.x, memento.y - self.y)

    def detach_view(self):
        self.canvas.delete(self.caption)
        self.canvas.delete(self.frame)
        self.canvas.delete(self.note_id)
        Component.detach_view(self)

    def accept(self, visitor, mode='DLR'):
        visitor.visit_note(self)

    def set_color(self, color):
        self.canvas.itemconfigure(self.frame, outline=color)

    def move(self, x, y):
        self.canvas.move(self.tag, x, y)
        self.x = self.x + x
        self.y = self.y + y

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = PropertyDlg(self)
        dlg.add_tab(CommonTab(dlg.notebook(), '共通', self))
        dlg.add_tab(NoteTab(dlg.notebook(), '信息', self))
        return dlg

    # 生成弹出菜单
    def create_popup(self, handler):
        menu = Menu(self.canvas, tearoff=False)
        menu.add_command(label='Property', command=(lambda: handler.on_command('SetProperty')))
        menu.add_command(label='Delete', command=(lambda: handler.on_command('Delete')))
        return menu

    def name_changed(self):
        try:
            self.canvas.itemconfigure(self.caption, text=self.name)
        except:
            pass # do nothing

    def get_note(self):
        return self.__note

    def set_note(self, note):
        self.handle_request(self, 'change_member',
                            {'getter': Note.get_note,
                             'setter': Note.set_note})
        self.__note = note
        try:
            self.canvas.itemconfigure(self.note_id, text=self.get_note())
        except:
            pass
        else:
            pass

    @property
    def note_id(self):
        return self.tag + '.note'

    @property
    def caption(self):
        return self.tag + '.caption'

    @property
    def frame(self):
        return self.tag + '.frame'