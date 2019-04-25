import sys
sys.path.append('..')
from Framework.Block import *

class HeatingController(Block):
    def __init__(self, cd = None, name = None):
        Block.__init__(self, cd, name,'煮饭控制器')

    def construct(self, parent):
        Block.construct(self, parent)
        InputPort(self.dict, 0, 'Md', '1:PID控制,2:模糊控制，3:AI控制').construct(self)
        InputPort(self.dict, 1, 'Run', '控制有效').construct(self)
        InputPort(self.dict, 2, 'Act', '温度实际值(°C）').construct(self)
        OutputPort(self.dict, 0, 'Out', '控制输出').construct(self)
        OutputPort(self.dict, 1, 'Sta', '控制器状态').construct(self)
        return self


