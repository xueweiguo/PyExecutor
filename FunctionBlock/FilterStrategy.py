from FunctionBlock.FbdStrategy import *


class FilterStrategy(FbdStrategy):
    def __init__(self, block=None, f=None):
        FbdStrategy.__init__(self, block)
        self.filter = f

    def start(self, context):
        if self.filter:
            self.filter.start()

    def stop(self, context):
        if self.filter:
            self.filter.stop()

    def execute(self, context):
        box = context.get_box(self.key)
        out = box.block.port('Out')
        if self.filter:
            value = self._input_values(context)
            in_value = float(value['In'])
            p1 = float(value['p1'])
            p2 = float(value['p2'])
            p3 = float(value['p3'])
            context.set_value(out.tag, self.filter.run(in_value, p1, p2, p3))
        else:
            context.set_value(out.tag, 0)
