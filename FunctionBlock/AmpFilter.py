import math
from FunctionBlock.Filter import *


class AmpFilter(Filter):
    def __init__(self):
        Filter.__init__(self)

    def start(self):
        pass

    def run(self, value, p1, p2, p3):
        return p1 * float(value)

    def stop(self):
        pass