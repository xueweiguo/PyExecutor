import sys


class TagFactory(object):
    def __init__(self, tag=''):
        self.current = 0
        self.f_tag = tag

    def createTag(self):
        id = str(self.current)
        self.current = self.current + 1
        id = 'Ex' + id
        return id

    @property
    def tag(self):
        return self.f_tag

    def set_dict(self, dict):
        pass
