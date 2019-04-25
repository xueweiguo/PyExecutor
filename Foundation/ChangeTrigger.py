from Foundation.Trigger import *


class ChangeTrigger(Trigger):
    def __init__(self, context, target):
        Trigger.__init__(self, context)
        self.prev = None
        self.target = target

    def entry(self):
        #print(eval(self.target))
        self.prev = eval(self.target)

    def check(self):
        return (self.prev != eval(self.target))
