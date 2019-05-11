from Framework.ExecContext import *
from FunctionBlock.ChannelManager import *


# 运算功能上下文
class FbdContext(ExecContext):
    def __init__(self):
        ExecContext.__init__(self)
        # 当前值
        self.value = {}
        # 保管箱，由利用者自行申请
        self.deposit_box = {}
        self.channel_mgr = ChannelManager()

    # 登录当前值
    def set_value(self, tag, value):
        self.value[tag] = value
        # 报告最新数据
        self.channel_mgr.report_data(tag, value)

    # 取得当前值
    def get_value(self, tag):
        value = self.value.get(tag)
        if value:
            return value
        else:
            return 0

    # 登录保管箱
    def register_box(self, key, box):
        self.deposit_box[key] = box

    # 撤销保管箱登录
    def unregister_box(self, key):
        self.deposit_box.pop(key)

    # 取得保管箱
    def get_box(self, key):
        return self.deposit_box.get(key)








