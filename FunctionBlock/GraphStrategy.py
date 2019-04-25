from FunctionBlock.FbdStrategy import *


class GraphStrategy(FbdStrategy):
    def __init__(self, block=None):
        FbdStrategy.__init__(self, block)
        self.display_names = {'In1': 'In1', 'In2': 'In2', 'In3': 'In3'}
        self.colors = {'In1': 'red', 'In2': 'blue', 'In3': 'green'}
        self.type = 'line'
        self.data = {}

    @staticmethod
    def graph_id(block, index):
        return block.tag + '.graph_' + str(index)

    @staticmethod
    def channel_name(index):
        return 'In{}'.format(index + 1)

    @staticmethod
    def graph_area(block):
        area_top = block.top +block.caption_height()
        area_left = block.left + 30
        area_right = block.right - 10
        area_bottom = block.bottom - 10
        return area_left, area_top, area_right, area_bottom


