import math
from FunctionBlock.Filter import *


class AbsFilter(Filter):
    def __init__(self):
        Filter.__init__(self)

    def start(self):
        pass

    def run(self, value, p1, p2, p3):
        return math.fabs(value)

    def stop(self):
        pass
