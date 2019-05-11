from FunctionBlock.FbdStrategy import *


class ValPanelStrategy(FbdStrategy):
    def __init__(self, block=None):
        FbdStrategy.__init__(self, block)
        self.display_names = {'In1': 'In1', 'In2': 'In2', 'In3': 'In3'}
        self.colors = {'In1': 'red', 'In2': 'blue', 'In3': 'black'}
        self.type = 'value'
        self.data = dict()
        self.width = 100

    def execute(self, context):
        box = context.get_box(self.key)
        value = self._input_values(context)

        if box.block.canvas:
            index = 0
            try:
                for port in box.block.iter('input_port'):
                    port_value = "{:.2f}".format(float(value[port.name]))
                    box.block.canvas.itemconfigure(self.value_id(box.block, index), text=port_value)
                    index = index + 1
            except Exception as e:
                print('ValPanelStrategy.execute error:', e)

    def attach_view(self, block):
        for i in range(0, 3):
            area = self.get_value_area(block, i)
            # value = block.port(block.input_names()[i]).value
            block.canvas.create_rectangle(area, tags=[block.tag, self.frame_id(block, i)], fill='white', outline='black')
            block.canvas.create_text(area[0], area[1], anchor=NW,
                               tags=[block.tag, self.value_id(block, i)])

    def detach_view(self, block):
        for i in range(0, 3):
            block.canvas.delete(self.frame_id(block, i))
            block.canvas.delete(self.value_id(block, i))

    def get_value_area(self, block, index):
        #暂定竖向排列
        height = DataPort.height()
        pt = block.port('In{}'.format(index+1)).point()
        area_top = pt[1] - height / 2
        area_left = block.left + 30
        area_right = block.right - 10
        return area_left, area_top, area_right, area_top + height

    def frame_id(self, block, index):
        return block.tag + '.frame' + str(index)

    def value_id(self, block, index):
        return block.tag + '.value' + str(index)
