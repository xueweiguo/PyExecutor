import sys
sys.path.append('..')
from ExFramework.ExBlock import *
from ExFramework.ExInputPort import *
from ExFramework.ExOutputPort import *

class SinFun(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self, name)
         self.children.append(ExInputPort('A', self))
         self.children.append(ExInputPort('t', self))
         self.children.append(ExInputPort('En', self))
         self.children.append(ExOutputPort('Out', self))



