from FunctionBlock.PackerDecorator import *


# BCC校验
class BccValidator(PackerDecorator):
    # 数据打包处理
    def pack(self, data):
        data = PackerDecorator.pack(self, data)
        # BCC校验,测试用
        data = data + '.bcc'
        return data

    # 数据解包处理
    def un_pack(self, data):
        # BCC确认, 测试用
        if data[len(data)-4:] == '.bcc':
            data = data[0 : len(data) - 4]
        data = PackerDecorator.un_pack(self, data)
        return data
