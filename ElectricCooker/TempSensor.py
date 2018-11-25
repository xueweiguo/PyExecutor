import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class TempSensor(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self,name)
         self.children.append(ExInputPort('En', self))
         self.children.append(ExOutputPort('Out', self))

