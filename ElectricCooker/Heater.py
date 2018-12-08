import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class Heater(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self,name, '加热器')
         self.append(ExInputPort('Mode', '1：模拟量，2：PWM', self))
         self.append(ExInputPort('In', '控制输入', self))




