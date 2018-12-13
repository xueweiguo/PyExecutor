#sys.path.append('..')
from ExFramework.ExBlock import *

class OpPanel(ExBlock):
    def __init__(self, parent, name):
        ExBlock.__init__(self, parent, name, '操作面板')

    def construct(self):
        ExBlock.construct(self)
        ExInputPort(self, 'En', '1:功能有效,0:功能禁止').construct()
        ExOutputPort(self, 'Md', '动作模式输出').construct()
        ExOutputPort(self, 'Start', '启动信号输出').construct()
        return self

