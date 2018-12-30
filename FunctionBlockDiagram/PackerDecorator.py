from FunctionBlockDiagram.DataPacker import *


# 数据封装器装饰基类
class PackerDecorator(DataPacker):
    def __init__(self, packer):
        self.packer = packer

    # 数据打包处理
    def pack(self, data):
        if self.packer:
            # 如果下级Packer是否已被指定，则调用器pack方法
            return self.packer.pack(data)
        else:
            # 什么也不做
            return data

    # 数据解包处理
    def un_pack(self, data):
        if self.packer:
            # 如果下级Packer是否已被指定，则调用其un_pack方法
            return self.packer.pack(data)
        else:
            # 什么也不做
            return data
