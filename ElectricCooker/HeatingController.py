import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class HeatingController(ExBlock):
    def __init__(self, parent, name):
        ExBlock.__init__(self, parent, name,'煮饭控制器')

    def construct(self):
        ExBlock.construct(self)
        ExInputPort(self, 'Md', '1:PID控制,2:模糊控制，3:AI控制').construct()
        ExInputPort(self, 'Run', '控制有效').construct()
        ExInputPort(self, 'Act', '温度实际值(°C）').construct()
        ExOutputPort(self, 'Out', '控制输出').construct()
        ExOutputPort(self, 'Sta', '控制器状态').construct()
        return self


