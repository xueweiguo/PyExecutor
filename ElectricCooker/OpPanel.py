#sys.path.append('..')
from ExFramework.ExBlock import *

class OpPanel(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self, name, '操作面板')
         self.append(ExInputPort('En', '1:功能有效,0:功能禁止', self))
         self.append(ExOutputPort('Md', '动作模式输出', self))
         self.append(ExOutputPort('Start', '启动信号输出', self))

