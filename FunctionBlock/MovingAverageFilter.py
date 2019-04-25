from FunctionBlock.Filter import *


class MovingAverageFilter(Filter):
    def __init__(self):
        Filter.__init__(self)
        self.buffer = None
        self.sum = 0

    def start(self):
        self.buffer = []
        self.sum = 0

    def run(self, value, p1, p2, p3):
        self.buffer.append(value)
        self.sum = self.sum + value
        while len(self.buffer) > max(int(p1), 1):
            self.sum = self.sum - self.buffer.pop(0)
        count = len(self.buffer)
        if count:
            return self.sum / count
        else:
            return 0

    def stop(self):
        self.buffer = None
