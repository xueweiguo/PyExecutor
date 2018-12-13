#import sys
from ExFramework.ExBlock import *
from ExFramework.ExInputPort import *


class GraphFun(ExBlock):
    def __init__(self, parent, name):
        ExBlock.__init__(self,parent, name, '趋势曲线图')

    def construct(self):
        ExBlock.construct(self)
        ExInputPort(self, 'In1', '曲线输入1').construct()
        ExInputPort(self, 'In2', '曲线输入2').construct()
        ExInputPort(self, 'In3', '曲线输入3').construct()
        ExInputPort(self, 'Mode', '表示形式,1:曲线，2：棒图，3：仪表').construct()
        return self


