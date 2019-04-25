from FunctionBlock.GraphStrategy import *


class TrendGraphStrategy(GraphStrategy):
    def __init__(self, block=None):
        GraphStrategy.__init__(self, block)

    def attach_canvas(self, block):
        area = self.graph_area(block)
        block.canvas.create_rectangle(area, tags=[block.tag, self.frame_id(block)], fill='white', outline='black')
        for i in range(0, 3):
            value = block.port(self.channel_name(i)).value
            block.canvas.create_line(0, 0, 0, 0, tags=[block.tag, self.graph_id(block, i)],
                                     fill=self.colors[self.channel_name(i)])

    def detach_canvas(self, block):
        block.canvas.delete(self.frame_id(block))
        for i in range(0, 3):
            block.canvas.delete(self.graph_id(block, i))

    def execute(self, context):
        box = context.get_box(self.key)
        value = self._input_values(context)
        try:
            if box.block.canvas:
                minimum = value['min']
                maximum = value['max']
                if maximum != minimum:
                    left, top, right, bottom = self.graph_area(box.block)

                    index = 0
                    for port in box.block.iter('input_port'):
                        out_port = port.data_source()
                        if out_port:
                            values = context.get_values(out_port.tag)
                            width = int(right - left)
                            if len(values) > width:
                                first = len(values) - width
                                values = values[first:]
                            coords = []
                            x = 0
                            for v in values:
                                coords.append(left + x)
                                v = max(minimum, min(maximum, v))
                                v = (v - minimum) / (maximum - minimum) * (bottom - top)
                                coords.append(bottom - v)
                                x = x + 1
                            if len(coords) >= 4:
                                box.block.canvas.coords(self.graph_id(box.block, index), coords)
                        index = index + 1
        except Exception as e:
            print('GraphStrategy.execute error:', e)

    def frame_id(self, block):
        return block.tag + '.graph_frame'