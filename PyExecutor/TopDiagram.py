from ExFramework.ExDiagram import *
from ExFramework.ExTagFactory import *

class TopDiagram(ExDiagram):
    def __init__(self, parent, name):
        ExDiagram.__init__(self, parent, name)
        self.tag_factory = ExTagFactory()
        self.__observers__ = []
    # 绑定ExObserver
    def attach_observer(self, observer):
        self.__observers__.append(observer)
    # 解绑ExObserver
    def detach(self, observer):
        self.__observers__.remove(observer)
    # 事件处理
    def handle_request(self, component, ext):
        #ExDiagram.handle_request(self, component, ext)
        if ext == 'create_tag':
            return self.tag_factory.createTag()
        if self.__observers__:
            for ob in self.__observers__:
                ob.update(component, ext)
        return None


