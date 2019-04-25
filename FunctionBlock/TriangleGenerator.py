from FunctionBlock.Generator import *


class TriangleGenerator(Generator):
    def __init__(self):
        Generator.__init__(self)

    def run(self, period):
        t_rate = self.get_percent(period)
        if t_rate < 0.5:
            return -1 + 4 * t_rate
        else:
            return 1 - 4 * (t_rate - 0.5)
