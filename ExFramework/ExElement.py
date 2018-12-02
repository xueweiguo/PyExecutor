from ExFramework.ExComponents import *

#功能块
class ExElement(ExComponent):
    def __init__(self, name, comment):
        ExComponent.__init__(self, name, comment)

    #生成属性对话框
    def create_property_dlg(self):
        pass

    # 生成弹出菜单
    def create_popup(self, handler):
        pass

    def rect(self):
        pass

