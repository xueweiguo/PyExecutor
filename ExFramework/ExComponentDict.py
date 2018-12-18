import sys
class ExComponentDict(object):
    __instance__ = None
    def __new__(cls):
        if not ExComponentDict.__instance__:
            ExComponentDict.__instance__ = super(ExComponentDict, cls).__new__(cls)
            ExComponentDict.__instance__.__dict__ = {}
        return ExComponentDict.__instance__

    def register(self, component):
        self.__dict__[component.tag] = component

    def unregister(self, component):
        self.__dict__.pop(component.tag)

    def component(self, tag):
        return self.__dict__[tag]

