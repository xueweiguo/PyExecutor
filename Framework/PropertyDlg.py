import asyncio
from tkinter.ttk import *
from Framework.PropertyTab import *


class PropertyDlg:
    def __init__(self, component):
        self.top = Toplevel(takefocus=True)
        self.component = component
        self.__notebook = Notebook(self.top)
        self.__notebook.pack(side="top", fill=BOTH, expand=True)
        self.apply = Button(self.top, text='Apply', takefocus=True, command=self.__apply)
        self.apply.pack(side=RIGHT, fill=BOTH)
        self.apply.bind("<Button-1>", self.__on_button)
        self.cancel = Button(self.top, text='Cancel', takefocus=True, command=self.__cancel)
        self.cancel.pack(side=RIGHT, fill=BOTH)
        self.cancel.bind("<Button-1>", self.__on_button)
        self.__tabs = []


    def notebook(self):
        return self.__notebook

    def add_tab(self, tab):
        self.__notebook.add(tab, text=tab.name)
        self.__notebook.pack(side="top", fill=BOTH, expand=True)
        self.__tabs.append(tab)

    def do_modal(self):
        self.top.grab_set()
        self.top.update()
        self.center_window()
        self.top.mainloop()

    def __apply(self):
        self.component.handle_request(self.component, 'begin_macro')
        for t in self.__tabs:
            t.apply()
        self.component.handle_request(self.component, 'end_macro')
        self.top.quit()
        self.top.destroy()

    def __cancel(self):
        self.top.quit()
        self.top.destroy()

    def __on_button(self, event):
        self.top.focus_force()

    def center_window(self):
        width = self.top.winfo_width()
        height = self.top.winfo_height()
        s_width = self.top.winfo_screenwidth()
        s_height = self.top.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (s_width - width) / 2, (s_height - height) / 2)
        self.top.geometry(size)