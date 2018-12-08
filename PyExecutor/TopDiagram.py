from ExFramework.ExDiagram import *
from ExFramework.ExTagFactory import *

class TopDiagram(ExDiagram):
    def __init__(self, name):
        ExDiagram.__init__(self, name)
        tag = ExTagFactory().createTag()
        self.set_tag(tag)
        self.__observers__ = []

    def attach(self, observer):
        self.__observers__.append(observer)

    def detach(self, observer):
        self.__observers__.remove(observer)

    def notify(self, component, ext):
        ExDiagram.notify(self, component, ext)
        if self.__observers__:
            for ob in self.__observers__:
                ob.update(component, ext)
