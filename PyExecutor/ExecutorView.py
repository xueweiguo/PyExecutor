from Framework.DiagramView import *
from Framework.EditCommand import *
from CanvasStateMachine import *


class ExecutorView(DiagramView):
    def __init__(self, parent, observer, color='lightyellow'):
        DiagramView.__init__(self, parent, observer, color)
        self.edit = None
        self.add = None
        self.debug = None
        self.build = None
        self.src_tag = None
        self.machine = CanvasStateMachine(self)
        self.machine.entry()
        self.make_toolbar(parent.toolbar)
        self.make_editbar(parent.edit_bar)
        self.make_menu(parent.top_menu)


    def set_diagram(self, diagram):
        DiagramView.set_diagram(self, diagram)
        self.machine.entry()

    # 构建工具条
    def make_editbar(self, toolbar):
        self.copy_btn = Button(toolbar, text='Copy', command=self.copy)
        self.copy_btn.pack(side=LEFT)
        self.paste_btn = Button(toolbar, text='Paste', command=self.copy)
        self.paste_btn.pack(side=LEFT)
        self.del_btn = Button(toolbar, text='Delete', command=self.delete)
        self.del_btn.pack(side=LEFT)
        self.undo_btn = Button(toolbar, text='Undo', command=self.undo)
        self.undo_btn.pack(side=LEFT)
        self.redo_btn = Button(toolbar, text='Redo', command=self.redo)
        self.redo_btn.pack(side=LEFT)

    # 构建工具栏
    def make_toolbar(self, toolbar):
        types = FactoryManager().factory('element').element_types()
        btn_list = []
        for b in toolbar.children.values():
            btn_list.append(b)
        for b in btn_list:
            b.destroy()

        for i in range(len(types)):
            btn = Button(toolbar, text=types[i], command=(lambda index=i: self.add_element(index)))
            btn.pack(side=LEFT)
            if types[i] == 'Input':
                self.input_btn = btn
            elif types[i] == 'Output':
                self.output_btn = btn

    # 构建菜单项
    def make_menu(self, menu):
        if not self.edit:
            self.edit = Menu(menu, tearoff=False)
            self.edit.add_command(label='Copy', command=self.copy, underline=0)
            self.edit.add_command(label='Paste', command=self.paste, underline=0)
            self.edit.add_command(label='Delete', command=self.delete, underline=0)
            menu.add_cascade(label='Edit', menu=self.edit, underline=0)

        # 添加图形要素菜单
        if self.add:
            self.add.delete(0, len(self.add._tclCommands) - 1)
        else:
            self.add = Menu(menu, tearoff=False)
            menu.add_cascade(label='Add', menu=self.add, underline=0)
        # 功能块子菜单
        types = FactoryManager().factory('element').element_types()
        for i in range(len(types)):
            self.add.add_command(label=types[i], command=(lambda index=i: self.add_element(index)))

        if not self.debug:
            self.debug = Menu(menu, tearoff=False)
            self.debug.add_command(label='Start', command=self.start_debug, underline=0)
            self.debug.add_command(label='Stop', command=self.stop_debug, underline=0)
            menu.add_cascade(label='Debug', menu=self.debug, underline=0)

        # 代码生成菜单
        if self.build:
            menu.delete(5)

        factory = FactoryManager().factory('builder')
        if factory:
            self.build = Menu(menu, tearoff=False)
            menu.add_cascade(label='Build', menu=self.build, underline=0)
            types = factory.builder_types()
            # 代码种类子菜单
            for i in range(len(types)):
                self.build.add_command(label=types[i], command=(lambda t=types[i]: self.build_source(t)))
        else:
            self.build = None

        self.update_ui()

    def create_popup(self):
        if self.diagram.dict[self.src_tag]:
            menu = Menu(self, tearoff=False)
            menu.add_command(label='Paste', command=self.paste)
            return menu
        else:
            return None

    # 构建功能块
    def add_element(self, index):
        types = FactoryManager().factory('element').element_types()
        self.element_type = types[index]
        self.canvas.configure(cursor='dotbox')

    def update(self):
        #print('PyEditorView.update()')
        if self.diagram:
            if self.diagram.parent:
                self.input_btn.configure(state=NORMAL)
                self.output_btn.configure(state=NORMAL)
            else:
                self.input_btn.configure(state=DISABLED)
                self.output_btn.configure(state=DISABLED)

            if self.diagram.redone():
                self.redo_btn.configure(state=DISABLED)
            else:
                self.redo_btn.configure(state=NORMAL)
            if self.diagram.undone():
                self.undo_btn.configure(state=DISABLED)
            else:
                self.undo_btn.configure(state=NORMAL)

    def update_ui(self):
        self.update()

        if self.is_running():
            self.debug.entryconfigure(0, state=DISABLED)
            self.debug.entryconfigure(1, state=ACTIVE)
        else:
            self.debug.entryconfigure(0, state=ACTIVE)
            self.debug.entryconfigure(1, state=DISABLED)

        if self.selected():
            self.copy_btn.configure(state=NORMAL)
            self.del_btn.configure(state=NORMAL)
        else:
            self.copy_btn.configure(state=DISABLED)
            self.del_btn.configure(state=DISABLED)

        if self.diagram and self.diagram.dict[self.src_tag]:
            self.paste_btn.configure(state=NORMAL)
        else:
            self.paste_btn.configure(state=DISABLED)

    def onDoubleClick(self, event):
        self.machine.event_handling('LButtonDoubleClick', self.grid(event))
        self.update_ui()

    def onLButtonDown(self, event):
        self.machine.event_handling('LButtonDown', self.grid(event))
        self.update_ui()

    def onRButtonDown(self, event):
        self.machine.event_handling('RButtonDown', self.grid(event))
        self.update_ui()

    def onLButtonMove(self, event):
        self.machine.event_handling('LButtonMove', self.grid(event))
        self.update_ui()

    def onMouseMove(self, event):
        self.machine.event_handling('MouseMove', self.grid(event))

    def onLButtonUp(self, event):
        self.machine.event_handling('LButtonUp', self.grid(event))
        self.update_ui()

    def onKey(self, event):
        self.machine.event_handling('Key', self.grid(event))
        self.update_ui()

    def delete(self):
        self.machine.event_handling('Command', 'Delete')

    def copy(self):
        self.machine.event_handling('Command', 'Copy')

    def paste(self):
        self.machine.event_handling('Command', 'Paste')







