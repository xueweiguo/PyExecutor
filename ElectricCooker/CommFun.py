from ExFramework.ExBlock import *

class CommFun(ExBlock):
    def __init__(self, parent, name, comment):
        ExBlock.__init__(self, parent, name, comment)
        self.port = None

    def construct(self):
        ExBlock.construct(self)
        ExInputPort(self, 'In1', '输入1').construct()
        ExInputPort(self, 'In2', '输入2').construct()
        ExInputPort(self, 'In3', '输入3').construct()
        ExOutputPort(self, 'Sta', '通信方式').construct()
        return self