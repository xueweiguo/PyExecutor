from tkinter import *
from tkinter.ttk import *
from Framework.PropertyTab import *
from FunctionBlock.CommPortFactory import *
from FunctionBlock.SectionPortProxy import *

from FunctionBlock.DesEncryptor import *
from FunctionBlock.IdeaEncryptor import *
from FunctionBlock.RsaEncryptor import *
from FunctionBlock.DsaEncryptor import *
from FunctionBlock.AesEncryptor import *
from FunctionBlock.BccValidator import *
from FunctionBlock.CrcValidator import *
from FunctionBlock.Md5Validator import *


class CommFunTab(PropertyTab):
    def __init__(self, parent, name, element):
        PropertyTab.__init__(self, parent, name, element)
        self.pack(side=TOP)

        pad = 2

        # 创建一个容器,
        port_frame = LabelFrame(self, text=" 端口设定 ")  # 创建一个容器，其父容器为win
        port_frame.grid(column=0, row=0, sticky=W, padx = pad, pady = pad)

        Label(port_frame, text="通信方式").grid(row=0, column=0, padx = pad, pady = pad, sticky=E)
        self.port = StringVar()
        port_list = Combobox(port_frame, width = 12, textvariable=self.port)
        port_list['values'] = ('未指定','Wifi','Bluetooth')
        port_list.state = 'readonly'
        port_list.current(1)
        port_list.grid(column=1, row=0, sticky=W, padx = pad, pady = pad)
        Label(port_frame, text='通信地址').grid(row=2, column=0, sticky=E, padx=pad, pady=1)
        self.address = StringVar()
        self.address.set('192.168.0.176')
        address = Entry(port_frame, textvariable=self.address)
        address.grid(row=2, column=1, sticky=W, padx=pad, pady=pad)

        data_frame = LabelFrame(self, text=" 数据处理 ", width = 200)  # 创建一个容器，其父容器为win
        data_frame.grid(column=0, row=1, sticky=W, padx = pad, pady = pad)

        Label(data_frame, text="加密方式").grid(row=0, column=0, sticky=E, padx = pad, pady = pad)
        self.security = StringVar()
        security_list = Combobox(data_frame, width=12, textvariable=self.security)
        security_list['values'] = ('不加密', 'DES', 'IDEA', 'RSA', 'DSA', 'AES')
        security_list.state = 'readonly'
        security_list.current(1)
        security_list.grid( row=0, column=1, sticky=W, padx = pad, pady = pad)
        Label(data_frame, text='密钥').grid(row=1, column=0, sticky=E, padx=pad, pady=pad)
        self.key = StringVar()
        self.key.set('123456')
        key = Entry(data_frame, textvariable=self.key)
        key.grid(row=1, column=1, sticky=W, padx=pad, pady=pad)
        Label(data_frame, text='校验方式').grid(row=2, column=0, sticky=E, padx=pad, pady=pad)
        self.ecc = StringVar()
        ecc_list = Combobox(data_frame, width=12, textvariable=self.ecc)
        ecc_list['values'] = ('无校验','BCC', 'CRC', 'MD5')
        ecc_list.state = 'readonly'
        ecc_list.current(1)
        ecc_list.grid(row=2, column=1, sticky=W, padx=pad, pady=pad)

        auth_frame = LabelFrame(self, text=" 用户认证 ")  # 创建一个容器，其父容器为win
        auth_frame.grid(column=0, row=2, sticky=W, padx=pad, pady=pad)
        Label(auth_frame, text="用户账号").grid(row=0, column=0, padx=pad, pady=pad, sticky=E)
        self.usr = StringVar()
        Entry(auth_frame, textvariable=self.usr).grid(row=0, column=1, sticky=W, padx=pad, pady=pad)
        Label(auth_frame, text='密码').grid(row=1, column=0, sticky=E, padx=pad, pady=1)
        self.pwd = StringVar()
        Entry(auth_frame, textvariable=self.pwd).grid(row=1, column=1, sticky=W, padx=pad, pady=pad)

    def apply(self):
        #设定通信端口
        factory = CommPortFactory()
        # 根据选择结果生成通信端口
        if self.port.get() == 'Wifi':
            port = factory.get_wifi(self.address.get())
        elif self.port.get() == 'Bluetooth':
            port = factory.get_bluetooth(self.address.get())
        else:
            port = None

        # 如果存在用户信息，另外生成端口代理
        if port:
            usr = self.usr.get()
            if usr:
                # 构建SectionPortProxy
                port = SectionPortProxy(port, usr, self.pwd.get())

        # 设置通信端口
        self.element.set_port(port)

        packer = None
        #  设定加密方式
        if self.security.get() == 'DES':
            packer = DesEncryptor(packer)
        elif  self.security.get() == 'IDEA':
            packer = IdeaEncryptor(packer)
        elif self.security.get() == 'RSA':
            packer = RsaEncryptor(packer)
        elif self.security.get() == 'DSA':
            packer = DsaEncryptor(packer)
        elif self.security.get() == 'AES':
            packer = AesEncryptor(packer)
        else:
            pass

        # 设定校验方式
        if self.ecc.get() == 'BCC':
            packer = BccValidator(packer)
        elif self.ecc.get() == 'CRC':
            packer = CrcValidator(packer)
        elif self.ecc.get() == 'MD5':
            packer = Md5Validator(packer)

        # 设定数据处理方式
        self.element.set_security(packer)

        #调用基类方法
        PropertyTab.apply(self)
