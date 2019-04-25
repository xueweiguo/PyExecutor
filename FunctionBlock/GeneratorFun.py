from FunctionBlock.FbdBlock import *
from FunctionBlock.GeneratorStrategy import *


class GeneratorFun(FbdBlock):
    def __init__(self, cd=None, name=""):
        FbdBlock.__init__(self, cd, name, '信号发生器')

    def construct_io(self, parent):
        InputPort(self.dict, 0, 'Type', '0：正弦波,1:方波,2:三角波').construct(self)
        InputPort(self.dict, 1, 'A', '振幅').construct(self)
        InputPort(self.dict, 2, 'T', '周期').construct(self)
        OutputPort(self.dict, 0, 'Out', '输出').construct(self)

    def create_strategy(self, t):
        strategy = GeneratorStrategy(self)
        if t == 0:
            strategy.set_generator(SinGenerator())
        elif t == 1:
            strategy.set_generator(SquareGenerator())
        elif t == 2:
            strategy.set_generator(TriangleGenerator())
        return strategy



