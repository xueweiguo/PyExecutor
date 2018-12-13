import sys
sys.path.append('..')
from ExFramework.ExBlock import *
from ExFramework.ExInputPort import *
from ExFramework.ExOutputPort import *
from FunctionBlockDiagram.MathFunTab import *

class MathFun(ExBlock):
    def __init__(self, parent, name):
        ExBlock.__init__(self, parent, name, '自定义数学运算\n支持四则运算,指数运算，三角函数等')

    def construct(self):
        ExBlock.construct(self)
        ExInputPort(self, 'In1','运算输入1').construct()
        ExInputPort(self, 'In2','运算输入2').construct()
        ExInputPort(self, 'In2','运算输入3').construct()
        ExOutputPort(self, 'Out1','运算输出1表达式,自由输入').construct()
        ExOutputPort(self, 'Out2','运算输出2表达式,自由输入').construct()
        return self

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = ExBlock.create_property_dlg(self)
        dlg.add_tab(MathFunTab(dlg.notebook(), '输出表达式', self))
        return dlg





