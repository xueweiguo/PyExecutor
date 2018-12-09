from ExFramework.ExNote import *
from ExFramework.ExCustomBlock import *

class ExComponentFactory(object):
    #构建连接线
    def make_connector(self):
        pass
    #取得支持的要素类型
    def element_types(self):
        return ['Custom', 'Note']
    #构建要素
    def make_element(self,type):
        if type == "Custom":
            return ExCustomBlock('Custom')
        elif type == "Note":
            return ExNote()


