import json
from FunctionBlockDiagram.CommFun import *

class CommInputFun(CommFun):
    #对象初始化
    def __init__(self, parent):
        CommFun.__init__(self, parent, 'CommInput', 'Recevie data from other device.')
    #构建数据通道
    def construct(self):
        CommFun.construct(self)
        ExOutputPort(self, 'CH1', '输入数据通道1').construct()
        ExOutputPort(self, 'CH2', '输入数据通道2').construct()
        return self
    #接收计算数据
    def recv_value(self):
        values = json.loads(self.recv_data())
        vi = 0
        data_ok = True
        for p in self.children():
            if isinstance(p, ExOutputPort) and (p.name != 'Sta'):
                if vi < len(values):
                    p.set_value(values[vi])
                    vi = vi + 1
                else:
                    data_ok = False
        self.set_status(data_ok)
    #发送反馈信息
    def send_response(self):
        response = []
        if self.get_status():
            response.append('Data OK')
        else:
            response.append('Data NG')
        self.send_data(json.dumps(response))



