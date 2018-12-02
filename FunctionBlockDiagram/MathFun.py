import sys
sys.path.append('..')
from ExFramework.ExBlock import *
from ExFramework.ExInputPort import *
from ExFramework.ExOutputPort import *
from FunctionBlockDiagram.MathPropertyDlg import *

class MathFun(ExBlock):
    def __init__(self, name):
        ExBlock.__init__(self, name, '自定义数学运算\n支持四则运算,指数运算，三角函数等')
        self.children.append(ExInputPort('In1','运算输入1', self))
        self.children.append(ExInputPort('In2','运算输入2',self))
        self.children.append(ExInputPort('In2','运算输入3',self))
        self.children.append(ExOutputPort('Out1','运算输出1表达式,自由输入',self))
        self.children.append(ExOutputPort('Out2','运算输出2表达式,自由输入',self))

    # 生成属性对话框
    def create_property_dlg(self):
        return MathPropertyDlg(self)




