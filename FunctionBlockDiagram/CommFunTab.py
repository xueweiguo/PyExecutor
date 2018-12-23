from tkinter import *
from tkinter.ttk import *
from ExFramework.ExPropertyTab import *
from FunctionBlockDiagram.WifiPort import *
from FunctionBlockDiagram.BluetoothPort import *
from FunctionBlockDiagram.Base64 import *
from FunctionBlockDiagram.Md5 import *

class CommFunTab(ExPropertyTab):
    def __init__(self, parent, name, element):
        ExPropertyTab.__init__(self, parent, name, element)
        self.pack(side=TOP)
        Label(self, text="通讯方式").grid(row=0, column=0, padx = 1, pady = 1, sticky=E)
        self.port = StringVar()
        port_list = Combobox(self, width = 12, textvariable=self.port)
        port_list['values'] = ('未指定','Wifi','Bluetooth')
        port_list.state = 'readonly'
        port_list.current(0)
        port_list.grid(column=1, row=0, sticky=W, padx = 1, pady = 1)
        Label(self, text="加密方式").grid(row=1, column=0, sticky=E, padx = 1, pady = 1)
        self.security = StringVar()
        security_list = Combobox(self, width=12, textvariable=self.security)
        security_list['values'] = ('未指定', 'Base64', 'MD5')
        security_list.state = 'readonly'
        security_list.current(0)
        security_list.grid( row=1, column=1, sticky=W, padx = 1, pady = 1)
        Label(self, text='通讯地址').grid(row=2, column=0, sticky=E, padx = 1, pady = 1)
        self.address = StringVar()
        address = Entry(self, textvariable=self.address)
        address.grid(row=2, column=1, sticky=W, padx = 1, pady = 1)

    def apply(self):
        #设定通讯方式
        if self.port.get() == 'Wifi':
            self.element.setPort(WifiPort(self.address.get()))
        elif self.port.get() == 'Bluetooth':
            self.element.setPort(BluetoothPort(self.address.get()))
        else:
            self.element.setPort(None)
        # 设定加密方式
        if self.security.get() == 'Base64':
            self.element.setSecurity(Base64())
        elif self.security.get() == 'Md5':
            self.element.setSecurity(Md5())
        else:
            self.element.setSecurity(None)
        #调用基类方法
        ExPropertyTab.apply(self)