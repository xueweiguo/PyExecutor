from FunctionBlockDiagram.PackerDecorator import *


# AES加密
class AesEncryptor(PackerDecorator):
    # 数据打包处理
    def pack(self, data):
        data = PackerDecorator.pack(self, data)
        # AES加密
        return data

    # 数据解包处理
    def un_pack(self, data):
        data = PackerDecorator.un_pack(self, data)
        # AES解密
        return data
