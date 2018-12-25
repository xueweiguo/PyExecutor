import json
from ExFramework.ExBlock import *
from FunctionBlockDiagram.CommFunTab import *

class CommFun(ExBlock):
    def __init__(self, parent, name, comment):
        ExBlock.__init__(self, parent, name, comment)
        self.port = None
        self.security = None
        self.status = None

    #构造状态输出端口
    def construct(self):
        ExBlock.construct(self)
        ExOutputPort(self, 'Sta', 'The status of communication.').construct()
        return self

    # 设定状态端口
    def set_status(self, status):
        self.findChild('Sta').set_value(status)

    # 取得状态端口
    def get_status(self):
        return self.findChild('Sta').get_value()

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = ExBlock.create_property_dlg(self)
        dlg.add_tab(CommFunTab(dlg.notebook(), '通讯', self))
        return dlg

    #设定通讯方式
    def set_port(self, port):
        self.port = port

    #设定加密方式
    def set_security(self, sec):
        self.security = sec

    #发送数据
    def send_list(self, list):
        return self.port.send_data(self.security.encode(json.dumps(list)))

    #接收数据
    def recv_list(self):
        return json.loads(self.security.decode(self.port.recv_data()))



