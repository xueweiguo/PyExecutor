from Framework.Block import *


class InputBlock(Block):
    def __init__(self, parent=None, name='', comment=''):
        Block.__init__(self, parent, name, comment)
        self.top_offset = 0
        self._caption_height = 0
        self.bottom_margin = 0

    def construct(self, parent):
        Block.construct(self, parent)
        OutputPort(self.dict, 0, '', '自定义模块输入').construct(self)
        return self
    
    def copy(self, memo):
        c = Block.copy(self, memo)
        c.top_offset = self.top_offset 
        c._caption_height = self._caption_height
        return c

    # 生成属性对话框
    def create_property_dlg(self):
        dlg = PropertyDlg(self)
        dlg.add_tab(CommonTab(dlg.notebook(), '共通', self))
        return dlg






