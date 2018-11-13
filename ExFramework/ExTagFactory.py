import sys
class ExTagFactory(object):
    _instance = None
    def __new__(cls):
        if not ExTagFactory._instance:
            ExTagFactory._instance = super(ExTagFactory, cls).__new__(cls)
            ExTagFactory._instance.current = 0
        return ExTagFactory._instance

    def createTag(self):
        id = 'Ex'+str(self.current)
        self.current = self.current + 1
        return id

    def serialize(self):
        return {'type':str(type(self)), 'current':self.current}