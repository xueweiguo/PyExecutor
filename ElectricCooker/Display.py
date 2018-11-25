import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class Display(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self,name)
         self.children.append(ExInputPort('In1', self))
         self.children.append(ExInputPort('In2', self))
         self.children.append(ExInputPort('In3', self))
         self.children.append(ExOutputPort('Sta', self))



