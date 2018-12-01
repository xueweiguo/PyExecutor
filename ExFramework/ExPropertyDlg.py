from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from ExFramework.ExElement import *

class ExPropertyDlg(Frame):
    def __init__(self, element):
        Frame.__init__(self, Toplevel())
        self.element = element
        self.pack()
        self.notebook = Notebook(self)
        for t in self.tabs():
            self.notebook.add(self.create_tab(t), text=t)
        self.notebook.pack(side="top", fill=BOTH, expand=True)
        Button(self, text='Apply', command=self.on_apply).pack(side=RIGHT, fill=BOTH)
        Button(self, text='Cancel', command=self.on_cancel).pack(side=RIGHT, fill=BOTH)

    def on_apply(self):
        pass

    def on_cancel(self):
        pass

    def tabs(self):
        return ['Common']

    def create_tab(self, title):
        if title == 'Common':
            tab = Frame(self)
            tab.pack(side=TOP)
            Label(tab, text="Tag").grid(row=0, column=0)
            tag = Entry(tab)
            tag.insert(0, self.element.tag())
            tag.configure(state='readonly')
            tag.grid(row=0, column=1)
            Label(tab, text="Name").grid(row=1, column=0)
            ent = Entry(tab)
            ent.insert(0, self.element.name())
            ent.grid(row=1, column=1)
            return tab

    def on_button(self, mode):
        Notebook.quit(self)

    def do_modal(self):
        #self.place(x=500,y=700,width=200,height=50)
      #  self.focus_set()
      #  self.grab_set()
        self.mainloop()
