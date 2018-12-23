from tkinter import *
from tkinter.ttk import *
from ExFramework.ExPropertyTab import *

class CommFunTab(ExPropertyTab):
    def __init__(self, parent, name, element):
        ExPropertyTab.__init__(self, parent, name, element)
        self.pack(side=TOP)
        Label(self, text="通讯方式").grid(row=0, column=0, padx = 1, pady = 1, sticky=E)
        protocal = Combobox(self, width = 12)
        protocal['values'] = ('未指定','Wifi','Bluetooth')
        protocal.state = 'readonly'
        protocal.grid(column=1, row=0, sticky=W, padx = 1, pady = 1)
        Label(self, text="加密方式").grid(row=1, column=0, sticky=E, padx = 1, pady = 1)
        security = Combobox(self, width=12)
        security['values'] = ('未指定', 'Base64', 'MD5')
        security.state = 'readonly'
        security.grid( row=1, column=1, sticky=W, padx = 1, pady = 1)
        Label(self, text='通讯地址').grid(row=2, column=0, sticky=E, padx = 1, pady = 1)
        address = Entry(self)
        address.grid(row=2, column=1, sticky=W, padx = 1, pady = 1)
