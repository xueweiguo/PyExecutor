import json
from Framework.Block import *
from FunctionBlock.CommFunTab import *

class CommFun(Block):
    def __init__(self, dict=None, name='', comment=''):
        Block.__init__(self, dict, name, comment)
        self.port = None
        self.security = None
        self.status = None

    #构造状态输出端口
    def construct(self, parent):
        Block.construct(self, parent)
        OutputPort(self.dict, 0, 'Sta', 'The status of communication.').construct(self)
        return self

    def copy(self, memo):
        c = Block.copy(self, memo)
        if self.port:
            c.port = copy.copy(self.port)
        else:
            c.port = None
        if self.security:
            c.security = copy.copy(self.security)
        else:
            c.security = None
        if self.status:
            c.status = copy.copy(self.status)
        else:
            c.status = None
        return c

    # 设定状态端口
    def set_status(self, status):
        self.port('Sta').set_value(status)

    # 取得状态端口
    def get_status(self):
        return self.port('Sta').get_value()

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = Block.create_property_dlg(self)
        dlg.add_tab(CommFunTab(dlg.notebook(), '通信', self))
        return dlg

    #设定端口
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



