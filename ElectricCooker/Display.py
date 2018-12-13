import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class Display(ExBlock):
    def __init__(self, parent, name):
        ExBlock.__init__(self, parent, name, '表示面板')

    def construct(self):
        ExBlock.construct(self)
        ExInputPort(self, 'In1', '输入1').construct()
        ExInputPort(self, 'In2', '输入2').construct()
        ExInputPort(self, 'In3', '输入3').construct()
        ExOutputPort(self, 'Sta', '状态输入').construct()
        return self



