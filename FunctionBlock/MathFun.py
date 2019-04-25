from math import *
from Framework.InputPort import *
from Framework.OutputPort import *
from FunctionBlock.FbdBlock import *
from FunctionBlock.MathFunStrategy import *
from FunctionBlock.MathFunTab import *


class MathFun(FbdBlock):
    def __init__(self, cd=None, name=''):
        FbdBlock.__init__(self, cd, name, '自定义数学运算\n支持四则运算,指数运算，三角函数等')

    def construct_io(self, parent):
        InputPort(self.dict, 0, 'In1','运算输入1').construct(self)
        InputPort(self.dict, 1, 'In2','运算输入2').construct(self)
        InputPort(self.dict, 2, 'In3','运算输入3').construct(self)
        InputPort(self.dict, 3, 'In4', '运算输入3').construct(self)
        OutputPort(self.dict, 0, 'Out1','运算输出1表达式,自由输入').construct(self)
        OutputPort(self.dict, 1, 'Out2','运算输出2表达式,自由输入').construct(self)

    def create_strategy(self, t):
        return MathFunStrategy(self)

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = Block.create_property_dlg(self)
        dlg.add_tab(MathFunTab(dlg.notebook(), '输出表达式', self))
        return dlg
