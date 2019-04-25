from tkinter import *
from tkinter.ttk import *


class ItemEdit(Entry):
    def __init__(self, view, row, col):
        bbox = view.bbox(row, col)
        Entry.__init__(self, view, width=int(bbox[2]/7))
        self.insert(INSERT, view.get_text(row, col))
        self.view = view
        self.row = row
        self.col = col
        self.place(x=bbox[0], y=bbox[1])
        self.bind('<FocusOut>', self.confirm)
        self.bind('<Return>', self.confirm)
        self.focus_set()

    def confirm(self, event):
        self.view.set_text(self.row, self.col, self.get())
        self.destroy()


class ListView(Treeview):
    def __init__(self, master, columns):
        Treeview.__init__(self, master)
        self["columns"] = columns
        self.editable = {}
        self.column('#0', minwidth=0, width=0)
        self.bind('<<TreeviewSelect>>', self.item_selected)
        self.bind('<Double-1>', self.item_double_clicked)  # 双击左键进入编辑

    def config_column(self, title, width, editable=False):
        self.column(title, width=width)
        self.heading(title, text=title)
        self.editable[title] = editable

    def item_double_clicked(self, event):
        column = self.identify_column(event.x)  # 列
        row = self.identify_row(event.y)  # 行
        if self.editable[self.heading(column)['text']]:
            ItemEdit(self, row, column)

    def item_selected(self, event):
        try:
            self.master.item_selected(event)
        except:
            pass
            # print(r"The master of ListView must implement the 'item_selected(self, event)' method.")

    def get_text(self, row, col):
        return self.set(row, col)

    def set_text(self, row, col, text):
        self.set(row, col, text)

    def sort_column(self, cols, reverse):
        key_pairs = []
        for iid in self.get_children(''):
            key = ''
            for c in cols:
                key = key + self.set(iid, c) + '#'
            key_pairs.append((key, iid))

        key_pairs.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (key, iid) in enumerate(key_pairs):
            self.move(iid, '', index)

