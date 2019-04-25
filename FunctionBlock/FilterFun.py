from FunctionBlock.FilterStrategy import *
from FunctionBlock.FbdBlock import *
from Framework.InputPort import *
from Framework.OutputPort import *

from FunctionBlock.ShiftTimeFilter import *
from FunctionBlock.MovingAverageFilter import *
from FunctionBlock.IntegrationFilter import *
from FunctionBlock.DifferentialFilter import *


class FilterFun(FbdBlock):
    def __init__(self, cd=None, name=""):
        FbdBlock.__init__(self, cd, name, '数字滤波器')

    def construct_io(self, parent):
        InputPort(self.dict, 0, 'In', '输入').construct(self)
        InputPort(self.dict, 1, 'Type', '0:时间平移,1:移动平均,2:积分,3:微分').construct(self)
        InputPort(self.dict, 2, 'p1', '参数1').construct(self)
        InputPort(self.dict, 3, 'p2', '参数2').construct(self)
        InputPort(self.dict, 4, 'p3', '参数3').construct(self)
        OutputPort(self.dict, 0, 'Out', '输出').construct(self)

    def create_strategy(self, t):
        if t == 0:
            return FilterStrategy(self, ShiftTimeFilter())
        elif t == 1:
            return FilterStrategy(self, MovingAverageFilter())
        elif t == 2:
            return FilterStrategy(self, IntegrationFilter())
        elif t == 3:
            return FilterStrategy(self, DifferentialFilter())
        else:
            return FilterStrategy(self)






