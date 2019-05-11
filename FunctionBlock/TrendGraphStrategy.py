from FunctionBlock.GraphStrategy import *
from FunctionBlock.TrendChannel import *


# 趋势曲线描画处理类
class TrendGraphStrategy(GraphStrategy):
    def __init__(self, block=None):
        GraphStrategy.__init__(self, block)
    # 挂接canvas对象
    def attach_view(self, block):
        area = self.graph_area(block)
        # 描画曲线表示区域边界
        block.canvas.create_rectangle(area, tags=[block.tag, self.frame_id(block)], fill='white', outline='black')
        for i in range(0, 3):
            value = block.port(self.channel_name(i)).value
            # fill设定内容决定曲线颜色
            block.canvas.create_line(0, 0, 0, 0, tags=[block.tag, self.graph_id(block, i)],
                                     fill=self.colors[self.channel_name(i)])
    # 取消挂接canvas
    def detach_view(self, block):
        block.canvas.delete(self.frame_id(block))
        for i in range(0, 3):
            block.canvas.delete(self.graph_id(block, i))
    #执行描画
    def execute(self, context):
        box = context.get_box(self.key)
        value = self._input_values(context)
        try:
            if box.block.canvas:
                minimum = value['min']
                maximum = value['max']
                if maximum != minimum:
                    # 取得描画范围
                    left, top, right, bottom = self.graph_area(box.block)
                    index = 0
                    # 依次处理每个输入通道
                    for port in box.block.iter('input_port'):
                        out_port = port.data_source()
                        if out_port:
                            # 取得描画数据
                            channel = context.channel_mgr.get(out_port.tag)
                            coords = channel.trend_coord(left, top, right, bottom, minimum, maximum)
                            # 执行描画
                            if len(coords) >= 4:
                                box.block.canvas.coords(self.graph_id(box.block, index), coords)
                        index = index + 1
        except Exception as e:
            print('GraphStrategy.execute error:', e)

    def frame_id(self, block):
        return block.tag + '.graph_frame'