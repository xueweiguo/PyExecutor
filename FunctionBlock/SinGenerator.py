from math import *
from FunctionBlock.Generator import *


class SinGenerator(Generator):
    def __init__(self):
        Generator.__init__(self)

    def run(self, period):
        t_rate = self.get_percent(period)
        return sin(2 * 3.1415926535897932 * t_rate)



