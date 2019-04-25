from FunctionBlock.PackerDecorator import *


# DES加密
class DesEncryptor(PackerDecorator):
    # 数据打包处理
    def pack(self, data):
        data = PackerDecorator.pack(self, data)
        # DES加密，详细省略
        data = data + '.des'
        return data

    # 数据解包处理
    def un_pack(self, data):
        # DES解密，详细省略
        if data[len(data)-4:] == '.des':
            data = data[0:len(data) - 4]
        data = PackerDecorator.un_pack(self, data)
        return data
