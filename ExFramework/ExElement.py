from ExFramework.ExComponents import *
from ExFramework.ExPropertyDlg import *

#功能要素
class ExElement(ExComponent):
    def __init__(self, name, comment):
        ExComponent.__init__(self, name, comment)

    #生成属性对话框
    def create_property_dlg(self):
        return ExPropertyDlg(self)

    # 生成弹出菜单
    def create_popup(self, handler):
        pass

    def rect(self):
        pass

