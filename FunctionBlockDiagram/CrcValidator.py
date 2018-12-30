from FunctionBlockDiagram.PackerDecorator import *


# CRC校验
class CrcValidator(PackerDecorator):
    # 数据打包处理
    def pack(self, data):
        data = PackerDecorator.pack(self, data)
        # CRC校验
        return data

    # 数据解包处理
    def un_pack(self, data):
        data = PackerDecorator.un_pack(self, data)
        # CRC确认
        return data
