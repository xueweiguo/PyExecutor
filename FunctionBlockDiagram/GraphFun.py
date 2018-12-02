#import sys
from ExFramework.ExBlock import *
from ExFramework.ExInputPort import *


class GraphFun(ExBlock):
    def __init__(self, name):
        ExBlock.__init__(self,name, '趋势曲线图')
        self.children.append(ExInputPort('In1', '曲线输入1', self))
        self.children.append(ExInputPort('In2', '曲线输入2', self))
        self.children.append(ExInputPort('In3', '曲线输入3', self))
        self.children.append(ExInputPort('Mode', '表示形式,1:曲线，2：棒图，3：仪表', self))


