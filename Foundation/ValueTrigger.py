from Foundation.Trigger import *


class ValueTrigger(Trigger):
    def __init__(self, context, target, value):
        Trigger.__init__(self, context)
        self.value = value
        self.target = target

    def entry(self):
        pass

    def check(self):
        return self.value == eval(self.target)