from Framework.Block import *

class Display(Block):
    def __init__(self, cd, name):
        Block.__init__(self, cd, name, '表示面板')

    def construct(self, parent):
        Block.construct(self, parent)
        InputPort(self.dict, 0, 'In1', '输入1').construct(self)
        InputPort(self.dict, 1, 'In2', '输入2').construct(self)
        InputPort(self.dict, 2, 'In3', '输入3').construct(self)
        OutputPort(self.dict, 0, 'Sta', '状态输入').construct(self)
        return self



