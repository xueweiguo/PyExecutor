from FunctionBlock.Filter import *


class ShiftValueFilter(Filter):
    def __init__(self):
        Filter.__init__(self)

    def start(self):
        pass

    def run(self, value, p1, p2, p3):
        return value + float(p1)

    def stop(self):
        pass

