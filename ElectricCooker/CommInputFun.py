from ElectricCooker.CommFun import *

class CommInputFun(CommFun):
    def __init__(self, parent):
        CommFun.__init__(self, parent, '命令输入', '接受外部控制命令')
        self.port = None

    def construct(self):
        CommFun.construct(self)
        ExOutputPort(self, 'Cmd', '命令数据').construct()
        return self