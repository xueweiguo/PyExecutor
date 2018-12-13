import sys
sys.path.append('..')
from ExFramework.ExBlock import *

from ExFramework.ExInputPort import *
from ExFramework.ExOutputPort import *

class CosFun(ExBlock):
    def __init__(self, parent, name):
        ExBlock.__init__(self, parent, name, '余弦信号发生器')

    def construct(self):
        ExBlock.construct(self)
        ExInputPort(self, 'A', '振幅').construct()
        ExInputPort(self, 'w', '角速度，单位为弧度/S').construct()
        ExInputPort(self, 't', '初始角度,单位为弧度').construct()
        ExInputPort(self, 'En', '有效').construct()
        ExOutputPort(self, 'Out','输出').construct()
        return self

