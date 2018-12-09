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
            return ExInputBlock('Input')
        elif type == "Output":
            return ExOutputBlock('Output')
        elif type == "Note":
            return ExNote()


