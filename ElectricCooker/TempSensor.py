import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class TempSensor(ExBlock):
    def __init__(self, parent, name):
        ExBlock.__init__(self, parent, name, '温度传感器')

    def construct(self):
        ExBlock.construct(self)
        ExInputPort(self, 'Tpye', '1:热电偶，2:热电阻，3：红外').construct()
        ExInputPort(self, 'En', '1:功能有效，0:功能禁止').construct()
        ExOutputPort(self, 'Out', '温度输出').construct()
        return self

