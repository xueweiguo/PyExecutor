from FunctionBlock.GraphStrategy import *


class BarGraphStrategy(GraphStrategy):
    def __init__(self, block=None):
        GraphStrategy.__init__(self, block)

    def attach_canvas(self, block):
        for i in range(0, 3):
            l,t,r,b = self.get_bar_area(block, i)
            block.canvas.create_rectangle(l, t, r, b, tags=[block.tag, self.frame_id(block, i)],
                                          outline='black')
            t = b #初始高度设为0
            block.canvas.create_rectangle(l, t, r, b, tags=[block.tag, self.graph_id(block, i)],
                                          fill=self.colors[self.channel_name(i)])

    def detach_canvas(self, block):
        for i in range(0, 3):
            block.canvas.delete(self.graph_id(block, i))
            block.canvas.delete(self.frame_id(block, i))

    # 棒图描画
    def execute(self, context):
        # 取得保管箱
        box = context.get_box(self.key)
        try:
            if box.block.canvas:
                # 取得输入数据
                value = self._input_values(context)
                minimum = value['min']
                maximum = value['max']
                if maximum != minimum:
                    index = 0
                    for port in box.block.iter('input_port'):
                        l,t,r,b = self.get_bar_area(box.block, index)
                        v = value[port.name]
                        v = max(minimum, min(maximum, v))
                        v = b - (v - minimum) / (maximum - minimum) * (b - t)
                        box.block.canvas.coords(self.graph_id(box.block, index), l, v, r, b)
                        index = index + 1
        except Exception as e:
            print('GraphStrategy.execute error:', e)

    def get_bar_area(self, block, index):
        #暂定竖向排列
        space = 10
        left, top, right, bottom = self.graph_area(block)
        width = (right - left - 2 * space) / 3
        left = left + (width + space) * index
        right = left + width
        return left, top, right, bottom

    def frame_id(self, block, index):
        return block.tag + '.graph_frame' + str(index)
