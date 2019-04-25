from FunctionBlock.FbdBlock import *
from FunctionBlock.BarGraphStrategy import *
from FunctionBlock.TrendGraphStrategy import *


class GraphFun(FbdBlock):
    def __init__(self, cd=None, name=''):
        FbdBlock.__init__(self, cd, name, '趋势曲线图')
        self.width = 200
        self.bottom_margin = 2

    # 构造输入/输出
    def construct_io(self, parent):
        InputPort(self.dict, 0, 'In1', '曲线输入1', 'red').construct(self)
        InputPort(self.dict, 1, 'In2', '曲线输入2', 'blue').construct(self)
        InputPort(self.dict, 2, 'In3', '曲线输入3', 'green').construct(self)
        InputPort(self.dict, 3, 'Type', '0：趋势曲线,1:柱状图').construct(self)
        self.port('Type').set_value(0)
        InputPort(self.dict, 4, 'min', '表示下限').construct(self)
        self.port('min').set_value(-10)
        InputPort(self.dict, 5, 'max', '表示上限').construct(self)
        self.port('max').set_value(10)

    # 生成策略对象
    def create_strategy(self, t):
        if t == 0:
            return TrendGraphStrategy(self)
        else:
            return BarGraphStrategy(self)
