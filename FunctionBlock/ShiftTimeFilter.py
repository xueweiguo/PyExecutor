from FunctionBlock.Filter import *


class ShiftTimeFilter(Filter):
    def __init__(self):
        Filter.__init__(self)
        self.buffer = None

    def start(self):
        self.buffer = []

    def run(self, value, p1, p2, p3):
        self.buffer.append(value)
        while len(self.buffer) > max(int(p1), 1):
            self.buffer.pop(0)
        return self.buffer[0]

    def stop(self):
        self.buffer = None
