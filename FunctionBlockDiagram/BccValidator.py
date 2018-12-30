from FunctionBlockDiagram.PackerDecorator import *


# BCC校验
class BccValidator(PackerDecorator):
    # 数据打包处理
    def pack(self, data):
        data = PackerDecorator.pack(self, data)
        # BCC校验
        return data

    # 数据解包处理
    def un_pack(self, data):
        data = PackerDecorator.un_pack(self, data)
        # BCC确认
        return data
