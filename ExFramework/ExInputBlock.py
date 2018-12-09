from ExFramework.ExBlock import *


class ExInputBlock(ExBlock):
    def __init__(self, name, comment):
        ExBlock.__init__(self, name, comment)
        self.append(ExOutputPort('Input', '自定义模块输入', self))