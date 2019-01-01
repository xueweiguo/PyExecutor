from ExFramework.ExDiagram import *
from ExFramework.ExTagFactory import *
from ExFramework.ExObservable import *

class TopDiagram(ExDiagram, ExObservable):
    def __init__(self, parent, name):
        ExDiagram.__init__(self, parent, name)
        ExObservable.__init__(self)
        self.tag_factory = ExTagFactory()

    # 事件处理
    def handle_request(self, component, ext):
        if ext == 'create_tag':
            return self.tag_factory.createTag()
        ExObservable.notify(self, component, ext)
        return None


