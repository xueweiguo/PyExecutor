import sys
sys.path.append('..')
from ExFramework.ExBlock import *
from ExFramework.ExInputPort import *
from ExFramework.ExOutputPort import *

class MathFun(ExBlock):
    def __init__(self, name):
        ExBlock.__init__(self,name)
        self.children.append(ExInputPort('In1',self))
        self.children.append(ExInputPort('In2',self))
        self.children.append(ExInputPort('In2',self))
        self.children.append(ExOutputPort('Out1',self))
        self.children.append(ExOutputPort('Out2',self))



