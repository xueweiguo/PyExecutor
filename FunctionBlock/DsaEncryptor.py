from FunctionBlock.PackerDecorator import *


# DSA加密
class DsaEncryptor(PackerDecorator):
    # 数据打包处理
    def pack(self, data):
        data = PackerDecorator.pack(self, data)
        # DSA加密
        return data

    # 数据解包处理
    def un_pack(self, data):
        data = PackerDecorator.un_pack(self, data)
        # DSA解密
        return data
