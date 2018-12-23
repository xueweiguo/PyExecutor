from ElectricCooker.CommFun import *

class CommOutputFun(CommFun):
    def __init__(self, parent):
        CommFun.__init__(self, parent, '数据输出模块', '输出控制过程数据')
        self.port = None

    def construct(self):
        CommFun.construct(self)
        ExInputPort(self, 'D1', '数据输出端口1').construct()
        ExInputPort(self, 'D2', '数据输出端口1').construct()
        return self