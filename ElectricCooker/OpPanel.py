#sys.path.append('..')
from Framework.Block import *

class OpPanel(Block):
    def __init__(self, cd=None, name=None):
        Block.__init__(self, cd, name, '操作面板')

    def construct(self, parent):
        Block.construct(self, parent)
        InputPort(self.dict, 0, 'En', '1:功能有效,0:功能禁止').construct(self)
        OutputPort(self.dict, 0, 'Md', '动作模式输出').construct(self)
        OutputPort(self.dict, 1, 'Start', '启动信号输出').construct(self)
        return self

