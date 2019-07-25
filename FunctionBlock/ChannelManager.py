from FunctionBlock.TrendChannel import *


# 共享TrendChannel管理类
class ChannelManager:
    def __init__(self):
        self.channels = {}

    # 取得TrendChannel
    def get(self, key):
        channel = self.channels.get(key)
        if not channel:
            channel = TrendChannel()
            self.channels[key] = channel
        return channel
    # 报告通道数据
    def report_data(self, key, value):
        channel = self.channels.get(key)
        if channel:
            channel.append(value)
