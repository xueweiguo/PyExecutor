from FunctionBlockDiagram.PackerDecorator import *


# IDEA加密
class IdeaEncryptor(PackerDecorator):
    # 数据打包处理
    def pack(self, data):
        data = PackerDecorator.pack(self, data)
        # IDEA加密
        return data

    # 数据解包处理
    def un_pack(self, data):
        data = PackerDecorator.un_pack(self, data)
        # IDEA解密
        return data
