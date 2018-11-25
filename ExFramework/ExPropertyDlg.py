from tkinter import *
from tkinter.messagebox import *
from PyExecutorFactory import *


class ExPropertyDlg(Frame):
    def __init__(self):
        Frame.__init__(self, TopLevel())
        self.pack()
        Label(self, text='Select the run mode of PyExecutor.').pack()
        for t in PyExecutorFactory().type_set:
            Button(self, text=t, command=(lambda arg=t: self.on_button(arg))).pack(side=TOP, fill=BOTH)

    def on_button(self, mode):
        Frame.quit(self)
