from tkinter import *
from tkinter.ttk import *
from ExFramework.ExInputPort import *
from ExFramework.ExPropertyDlg import *

class ExNotePropertyDlg(ExPropertyDlg):
    def __init__(self, element):
        ExPropertyDlg.__init__(self, element)

    def tabs(self):
        ts = ExPropertyDlg.tabs(self)
        ts.append('note')
        return ts

    def create_tab(self, title):
        if title == "note":
            return self.create_note_tab()
        else:
            return ExPropertyDlg.create_tab(self, title)

    def create_note_tab(self):
        tab = Frame(self)
        tab.pack(side=TOP)
        self.text = Text(tab, height=10, width=30)
        self.text.insert(INSERT, "在此处自由输入")
        self.text.pack()
        return tab
