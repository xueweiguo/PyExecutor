from ExFramework.ExNote import *
from ExFramework.ExCustomBlock import *
from ExFramework.ExInputBlock import *
from ExFramework.ExOutputBlock import *

class ExComponentFactory(object):
    #构建连接线
    def make_connector(self, parent):
        pass
    #取得支持的要素类型
    def element_types(self):
        return ['Custom', 'Input', 'Output','Note']
    #构建要素
    def make_element(self,parent, type):
        if type == "Custom":
            return ExCustomBlock(parent, 'Custom').construct()
        elif type == "Input":
            return ExInputBlock(parent, 'Input', '用户取得自定义功能的输入数据').construct()
        elif type == "Output":
            return ExOutputBlock(parent, 'Output','用于设定用户自定义模块的输出数据').construct()
        elif type == "Note":
            return ExNote(parent).construct()


