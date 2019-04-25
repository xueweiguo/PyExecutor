from FunctionBlock.FbdStrategy import *
from FunctionBlock.SinGenerator import *
from FunctionBlock.SquareGenerator import *
from FunctionBlock.TriangleGenerator import *


class GeneratorStrategy(FbdStrategy):
    def __init__(self, block=None):
        FbdStrategy.__init__(self, block)
        self.generator = None

    def __copy__(self):
        strategy = FbdStrategy.__copy__(self)
        strategy.generator = copy.deepcopy(self.generator)
        return strategy

    def set_generator(self, g):
        self.generator = g

    def execute(self, context):
        box = context.get_box(self.key)
        value = self._input_values(context)
        out = box.block.port('Out')
        if self.generator:
            period = float(value.get('T'))
            context.set_value(out.tag, float(value['A']) * self.generator.run(period))
        else:
            return 0

