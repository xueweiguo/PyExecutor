from ElectricCooker.CommFun import *

class HuaweiCommFun(CommFun):
    def __init__(self, parent):
        CommFun.__init__(self, parent, '华为通信', '华为通信功能模块')
        self.port = None

    def construct(self):
        CommFun.construct(self)
        return self