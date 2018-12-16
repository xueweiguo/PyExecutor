from ExFramework.ExBlock import *


class ExOutputBlock(ExBlock):
    def __init__(self, parent, name, comment):
        ExBlock.__init__(self, parent, name, comment)

    def construct(self):
        ExBlock.construct(self)
        ExInputPort(self, '', '自定义功能输出').construct()
        return self

    def port_start(self):
        return self.top() + 5




