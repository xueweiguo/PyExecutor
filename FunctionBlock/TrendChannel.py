# 趋势曲线表示通道类
class TrendChannel:
    def __init__(self):
        self.values = []

    # 添加描画数据
    def append(self, value):
        self.values.append(value)
        if len(self.values) > 200:
            self.values.pop(0)

    # 根据描画范围和表示上下限计算描画坐标
    def trend_coord(self, left, top, right, bottom, low_value, high_value):
        # 执行描画
        width = int(right - left)
        if len(self.values) > width:
            first = len(self.values) - width
        else:
            first = 0
        coord = []
        index = 0
        for v in self.values:
            if index > first:
                coord.append(left + index - first)
                v = max(low_value, min(high_value, v))
                v = (v - low_value) / (high_value - low_value) * (bottom - top)
                coord.append(bottom - v)
            index = index + 1
        return coord