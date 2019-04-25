from FunctionBlock.Filter import *


class IntegrationFilter(Filter):
    def __init__(self):
        Filter.__init__(self)
        self.sum = 0

    def start(self):
        self.sum = 0

    def run(self, value, p1, p2, p3):
        self.sum = self.sum + value
        return self.sum

    def stop(self):
        self.sum = 0
