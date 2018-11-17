import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class HeatingController(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self,name)
         self.children.append(ExInputPort('Mode', self))
         self.children.append(ExInputPort('Run', self))
         self.children.append(ExInputPort('TempAct', self))
         self.children.append(ExOutputPort('Output', self))
         self.children.append(ExOutputPort('Status', self))


