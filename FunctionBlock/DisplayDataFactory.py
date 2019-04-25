from FunctionBlock.ValueData import *
from FunctionBlock.BufferData import *


class DisplayDataFactory:
    def __init__(self):
        self.buffer_data = dict()

    #取得数值数据
    def get_value_data(self, key):
        data = ValueData(key)

    #取得曲线数据
    def get_buffer_data(self, key):
        data = self.buffer_data.get(key)
        if data:
            return data
        data = BufferData()
        self.buffer_data[key] = data
        return data


