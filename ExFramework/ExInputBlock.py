from ExFramework.ExBlock import *


class ExInputBlock(ExBlock):
    def __init__(self, parent, name, comment):
        ExBlock.__init__(self, parent, name, comment)

    def construct(self):
        ExBlock.construct(self)
        ExOutputPort(self, '', '自定义模块输入').construct()
        return self

    def port_start(self):
        return self.top + 5


