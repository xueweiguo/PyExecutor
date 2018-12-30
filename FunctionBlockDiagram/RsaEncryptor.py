from FunctionBlockDiagram.PackerDecorator import *


# RSA加密
class RsaEncryptor(PackerDecorator):
    # 数据打包处理
    def pack(self, data):
        data = PackerDecorator.pack(self, data)
        # RSA加密
        return data

    # 数据解包处理
    def un_pack(self, data):
        data = PackerDecorator.un_pack(self, data)
        # RSA解密
        return data
