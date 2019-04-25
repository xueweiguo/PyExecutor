from tkinter import *


class PropertyTab(Frame):
    def __init__(self, parent, name, element):
        Frame.__init__(self, parent)
        self.__element = element
        self.__name = name

    @property
    def element(self):
        return self.__element

    @property
    def name(self):
        return self.__name

    def apply(self):
        pass