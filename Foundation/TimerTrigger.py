import time
from Foundation.Trigger import *


class TimerTrigger(Trigger):
    def __init__(self, context, timer):
        Trigger.__init__(self, context)
        self.start = 0
        self.timer = timer

    def entry(self):
        self.start = time.time()

    def check(self):
        return (time.time() - self.start) > self.timer
