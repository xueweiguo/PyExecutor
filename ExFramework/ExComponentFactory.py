from ExFramework.ExNote import *
class ExComponentFactory(object):
    #构建连接线
    def makeConnector(self):
        pass
    #取得支持的要素类型
    def elementTypes(self):
        return ['Note']
    #构建要素
    def makeElement(self,type):
        if type == "Note":
            return ExNote()
    #系列化编码器
    def jsonEncoder(self):
        pass



