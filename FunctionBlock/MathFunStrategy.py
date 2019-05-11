from FunctionBlock.FbdStrategy import *
from Interpreter.Calculator import *

#数学计算用策略
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

    #执行数学计算
    def execute(self, context):
        box = context.get_box(self.key)
        value = self._input_values(context)

        # 构造计算器对象
        c = Calculator()
        # 指定外部数据
        c.set_value('In1', str(value['In1']))
        c.set_value('In2', str(value['In2']))
        c.set_value('In3', str(value['In3']))
        c.set_value('In4', str(value['In4']))

        for port in box.block.iter('output_port'):
            if len(self.exprs[port.name][0]):
                exp = self.exprs[port.name][0]
                # 计算表达式结果并输出
                context.set_value(port.tag, c.calculate(exp))

