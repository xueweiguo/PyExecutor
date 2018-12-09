from ExFramework.ExBlock import *


class ExOutputBlock(ExBlock):
    def __init__(self, name, comment):
        ExBlock.__init__(self, name, comment)
        self.append(ExInputPort('Out', '自定义功能输出', self))
