from FunctionBlock.FbdStrategy import *


class MathFunStrategy(FbdStrategy):
    def __init__(self, block=None):
        FbdStrategy.__init__(self, block)
        if block:
            self.exprs = dict()
            for port in block.iter('output_port'):
                self.exprs[port.name] = '', ''
        else:
            self.exprs = None

    def __copy__(self):
        strategy = FbdStrategy.__copy__(self)
        strategy.exprs = copy.deepcopy(self.exprs)
        return strategy

    def execute(self, context):
        box = context.get_box(self.key)
        value = self._input_values(context)

        # for self.expr
        In1 = value['In1']
        In2 = value['In2']
        In3 = value['In3']
        In4 = value['In4']

        for port in box.block.iter('output_port'):
            try:
                if len(self.exprs[port.name][0]):
                    context.set_value(port.tag, eval(self.exprs[port.name][0]))
            except Exception as e:
                print('Error in expr of', port.name, ':', e, '.')


