from FunctionBlock.FbdBlock import *
from FunctionBlock.ValPanelStrategy import *


class ValPanelFun(FbdBlock):
    def __init__(self, cd=None, name=''):
        FbdBlock.__init__(self, cd, name, '数字表示面板')

    def construct_io(self, parent):
        InputPort(self.dict, 0, 'In1', '输入1').construct(self)
        InputPort(self.dict, 1, 'In2', '输入2').construct(self)
        InputPort(self.dict, 2, 'In3', '输入3').construct(self)

    def create_strategy(self, t):
        return ValPanelStrategy(self)
