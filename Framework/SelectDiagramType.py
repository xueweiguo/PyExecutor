from tkinter import *
from Framework.FactoryManager import *


class SelectDiagramType:
    def __init__(self):
        self.master = None

    def construct(self, master):
        self.master = master
        Label(master, text='Select the type of the  diagram.').pack()
        modes = FactoryManager().modes()
        for m in modes:
            b = Button(master, text=m, command=(lambda arg=m: self.on_button(arg)))
            b.pack(side=TOP, fill=BOTH)

    def on_button(self, mode):
        FactoryManager().mode = mode
        self.master.close()

