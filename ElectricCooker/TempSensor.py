from Framework.Block import *


class TempSensor(Block):
    def __init__(self, cd=None, name=None):
        Block.__init__(self, cd, name, '温度传感器')

    def construct(self, parent):
        Block.construct(self, parent)
        InputPort(self.dict, 0, 'Type', '1:热电偶，2:热电阻，3：红外').construct(self)
        InputPort(self.dict, 1, 'En', '1:功能有效，0:功能禁止').construct(self)
        OutputPort(self.dict, 0, 'Out', '温度输出').construct(self)
        return self

