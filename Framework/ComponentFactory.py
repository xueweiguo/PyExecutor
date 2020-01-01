from Framework.Note import *
from Framework.CustomBlock import *
from Framework.InputBlock import *
from Framework.OutputBlock import *


class ComponentFactory(object):
    # 构建连接线
    def make_connector(self, parent):
        raise NotImplementedError

    # 取得支持的要素类型
    def element_types(self):
        return ['Custom', 'Input', 'Output', 'Note']

    # 建要素
    def make_element(self, cd, parent, type):
        if type == "Custom":
            return CustomBlock(cd, 'Custom').construct(parent)
        elif type == "Input":
            return InputBlock(cd, 'Input', '用户取得自定义功能的输入数据').construct(parent)
        elif type == "Output":
            return OutputBlock(cd, 'Output','用于设定用户自定义模块的输出数据').construct(parent)
        elif type == "Note":
            return Note(cd).construct(parent)

    # 生成运行上下文
    def make_context(self):
        raise NotImplementedError


