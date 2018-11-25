from ExFramework.ExTrigger import *

class ExChangeTrigger(ExTrigger):
    def __init__(self, context, target):
        ExTrigger.__init__(self, context)
        self.prev = None
        self.target = target

    def entry(self):
        #print(eval(self.target))
        self.prev = eval(self.target)

    def check(self):
        return (self.prev != eval(self.target))
