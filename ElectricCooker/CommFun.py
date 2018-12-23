from ExFramework.ExBlock import *
from ElectricCooker.CommFunTab import *

class CommFun(ExBlock):
    def __init__(self, parent, name, comment):
        ExBlock.__init__(self, parent, name, comment)
        self.protocal = None
        self.port = None

    def construct(self):
        ExBlock.construct(self)
        ExOutputPort(self, 'Sta', '通讯状态').construct()
        return self

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = ExBlock.create_property_dlg(self)
        dlg.add_tab(CommFunTab(dlg.notebook(), '通讯', self))
        return dlg