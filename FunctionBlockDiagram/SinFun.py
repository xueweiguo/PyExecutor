import sys
sys.path.append('..')
from ExFramework.ExBlock import *
from ExFramework.ExInputPort import *
from ExFramework.ExOutputPort import *

class SinFun(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self, name, '正弦信号发生器')
         self.append(ExInputPort('A', '振幅', self))
         self.append(ExInputPort('w', '角速度，单位为弧度/S', self))
         self.append(ExInputPort('t', '初始角度,单位为弧度', self))
         self.append(ExInputPort('En', '有效', self))
         self.append(ExOutputPort('Out', '输出', self))



