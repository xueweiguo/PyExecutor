from FunctionBlock.Filter import *


class DifferentialFilter(Filter):
    def __init__(self):
        Filter.__init__(self)
        self.prev = 0
        self.valid = False

    def start(self):
        self.valid = False
        self.prev = 0

    def run(self, value, p1, p2, p3):
        if self.valid:
            ret = value - self.prev
            self.prev = value
            return ret
        else:
            self.prev = value
            self.valid = True
            return 0

    def stop(self):
        self.valid = False
        self.prev = 0