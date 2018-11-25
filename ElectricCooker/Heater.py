import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class Heater(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self,name)
         self.children.append(ExInputPort('In', self))




