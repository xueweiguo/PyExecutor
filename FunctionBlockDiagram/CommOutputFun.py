from FunctionBlockDiagram.CommFun import *

class CommOutputFun(CommFun):
    def __init__(self, parent):
        CommFun.__init__(self, parent, 'ComOutput', '计算结果输出')
        self.port = None

    #构建数据通道
    def construct(self):
        CommFun.construct(self)
        ExInputPort(self, 'CH1', '数据输出端口1').construct()
        ExInputPort(self, 'CH2', '数据输出端口2').construct()
        return self

    #发送计算结果
    def send_value(self, value):
        values = [self.findChild('CH1').value(),self.findChild('CH2').value()]
        self.send_list(values)

    #接收反馈信息
    def recv_response(self):
        resp = self.recv_list()
        if len(resp) == 1 and resp[0] == 'VALUE_OK':
            self.set_status(True)
        else:
            self.set_status(False)

