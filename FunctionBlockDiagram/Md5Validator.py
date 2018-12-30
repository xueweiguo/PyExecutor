from FunctionBlockDiagram.PackerDecorator import *


# MD5校验
class Md5Validator(PackerDecorator):
    # 数据打包处理
    def pack(self, data):
        data = PackerDecorator.pack(self, data)
        # MD5校验
        return data

    # 数据解包处理
    def un_pack(self, data):
        data = PackerDecorator.un_pack(self, data)
        # MD5确认
        return data
