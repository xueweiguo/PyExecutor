import sys
class ExTagFactory(object):
    def __init__(self):
        self.current = 0

    def createTag(self):
        id = 'Ex'+str(self.current)
        self.current = self.current + 1
        return id

    def serialize(self):
        return {'type':str(type(self)), 'current':self.current}