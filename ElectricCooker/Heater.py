import sys
sys.path.append('..')
from Framework.Block import *

class Heater(Block):
    def __init__(self, cd=None, name=None):
        Block.__init__(self, cd, name, '加热器')

    def construct(self, parent):
        Block.construct(self, parent)
        InputPort(self.dict, 0, 'Mode', '1：模拟量，2：PWM').construct(self)
        InputPort(self.dict, 1, 'In', '控制输入').construct(self)
        return self




