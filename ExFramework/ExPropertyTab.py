from tkinter import *
class ExPropertyTab(Frame):
    def __init__(self, parent, name, element):
        Frame.__init__(self,parent)
        self.__element__ = element
        self.__name__ = name

    @property
    def element(self):
        return self.__element__

    @property
    def name(self):
        return self.__name__

    def apply(self):
        pass