from ExFramework.ExNote import *
from ExFramework.ExCustomBlock import *
from ExFramework.ExInputBlock import *
from ExFramework.ExOutputBlock import *

class ExComponentFactory(object):
    #构建连接线
    def make_connector(self):
        pass
    #取得支持的要素类型
    def element_types(self):
        return ['Custom', 'Input', 'Output','Note']
    #构建要素
    def make_element(self,type):
        if type == "Custom":
            return ExCustomBlock('Custom')
        elif type == "Input":
            return ExInputBlock('Input', '用户取得自定义功能的输入数据')
        elif type == "Output":
            return ExOutputBlock('Output','用于设定用户自定义模块的输出数据')
        elif type == "Note":
            return ExNote()


