from ExFramework.ExComposite import *
from ExFramework.ExPropertyDlg import *
from ExFramework.ExCommonTab import *

#功能要素
class ExElement(ExComposite):
    def __init__(self, parent, name, comment):
        ExComposite.__init__(self, parent, name, comment)

    #生成属性对话框
    def create_property_dlg(self):
        dlg = ExPropertyDlg(self)
        dlg.add_tab(ExCommonTab(dlg.notebook(), '共通', self))
        return dlg

    # 生成弹出菜单
    def create_popup(self, handler):
        pass




