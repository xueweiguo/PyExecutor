import sys
sys.path.append('..')
from ExFramework.ExState import *

class ExStateMachine(ExState):
    def __init__(self, owner, context):
        ExState.__init__(self, owner, context)
        print(self, context)

    def eventHandling(self, type, event):
        ExState.eventHandling(self, type, event)

