import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class TempSensor(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self, name, '温度传感器')
         self.append(ExInputPort('Tpye', '1:热电偶，2:热电阻，3：红外', self))
         self.append(ExInputPort('En', '1:功能有效，0:功能禁止', self))
         self.append(ExOutputPort('Out', '温度输出', self))

