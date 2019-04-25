from FunctionBlock.FbdBlock import *
from FunctionBlock.CommOutStrategy import *
from FunctionBlock.CommFunTab import *


class CommOutputFun(FbdBlock):
    def __init__(self, cd=None):
        FbdBlock.__init__(self, cd, 'ComOutput', '计算结果输出')
        self.port = None

    #构建数据通道
    def construct_io(self, parent):
        InputPort(self.dict, 1, 'CH1', '数据输出端口1').construct(self)
        InputPort(self.dict, 2, 'CH2', '数据输出端口2').construct(self)
        return self

    # 生成策略对象
    def create_strategy(self, t):
        return CommOutStrategy()

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = Block.create_property_dlg(self)
        dlg.add_tab(CommFunTab(dlg.notebook(), '通信', self.strategy))
        return dlg

    #发送计算结果
    def send_value(self, value):
        values = [self.find_port('CH1').value(), self.find_port('CH2').value()]
        self.send_list(values)

    #接收反馈信息
    def recv_response(self):
        resp = self.recv_list()
        if len(resp) == 1 and resp[0] == 'VALUE_OK':
            self.set_status(True)
        else:
            self.set_status(False)

