import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class HeatingController(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self,name)
         self.children.append(ExInputPort('Md', self))
         self.children.append(ExInputPort('Run', self))
         self.children.append(ExInputPort('Act', self))
         self.children.append(ExOutputPort('Out', self))
         self.children.append(ExOutputPort('Sta', self))


