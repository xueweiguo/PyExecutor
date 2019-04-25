from Framework.ExecContext import *


# 运算功能上下文
class FbdContext(ExecContext):
    def __init__(self):
        ExecContext.__init__(self)
        # 当前值
        self.value = {}
        # 历史数据
        self.values = {}
        # 保管箱，由利用者自行申请
        self.deposit_box = {}

    # 登录当前值
    def set_value(self, tag, value):
        self.value[tag] = value
        values = self.values.get(tag)
        # 如果存在历史数据列表，则同时存储
        if values:
            values.append(value)
            if len(values) > 200:
                values.pop(0)

    # 取得当前值
    def get_value(self, tag):
        value = self.value.get(tag)
        if value:
            return value
        else:
            return 0

    # 取得历史数据
    def get_values(self, tag):
        values = self.values.get(tag)
        if not values:
            values = []
            values.append(self.get_value(tag))
            self.values[tag] = values
        return values

    # 登录保管箱
    def register_box(self, key, box):
        self.deposit_box[key] = box

    # 撤销保管箱登录
    def unregister_box(self, key):
        self.deposit_box.pop(key)

    # 取得保管箱
    def get_box(self, key):
        return self.deposit_box.get(key)








