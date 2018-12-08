import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class HeatingController(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self,name,'煮饭控制器')
         self.append(ExInputPort('Md', '1:PID控制,2:模糊控制，3:AI控制', self))
         self.append(ExInputPort('Run', '控制有效', self))
         self.append(ExInputPort('Act', '温度实际值(°C）', self))
         self.append(ExOutputPort('Out', '控制输出', self))
         self.append(ExOutputPort('Sta', '控制器状态', self))


