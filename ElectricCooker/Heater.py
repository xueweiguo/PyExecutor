import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class Heater(ExBlock):
    def __init__(self, parent, name):
        ExBlock.__init__(self, parent, name, '加热器')

    def construct(self):
        ExBlock.construct(self)
        ExInputPort(self, 'Mode', '1：模拟量，2：PWM').construct()
        ExInputPort(self, 'In', '控制输入').construct()
        return self




