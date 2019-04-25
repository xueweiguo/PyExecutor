from FunctionBlock.FbdBlock import *
from FunctionBlock.CommInStrategy import *
from FunctionBlock.CommFunTab import *


class CommInputFun(FbdBlock):
    # 对象初始化
    def __init__(self, parent=None):
        FbdBlock.__init__(self, parent, 'CommInput', 'Recevie data from other device.')

    # 构建数据通道
    def construct_io(self, parent):
        OutputPort(self.dict, 1, 'CH1', '输入数据通道1').construct(self)
        OutputPort(self.dict, 2, 'CH2', '输入数据通道2').construct(self)
        return self

    # 生成策略对象
    def create_strategy(self, t):
        return CommInStrategy(self)

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = Block.create_property_dlg(self)
        dlg.add_tab(CommFunTab(dlg.notebook(), '通信', self.strategy))
        return dlg




