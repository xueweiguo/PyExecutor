from ExFramework.ExDiagram import *
from ExFramework.ExTagFactory import *
from ExFramework.ExObservable import *

class TopDiagram(ExDiagram, ExObservable):
    def __init__(self, parent, name):
        ExDiagram.__init__(self, parent, name)
        ExObservable.__init__(self)
        self.tag_factory = ExTagFactory()
        self.factorys = dict()

    # 事件处理
    def handle_request(self, component, req, params=None):
        if req == 'create_tag':
            return self.tag_factory.createTag()
        elif req == 'get_factory':
            return self.get_factory(params[0])
        ExObservable.notify(self, component, req)
        return None

    def get_factory(self, class_info):
        factory = self.factorys.get(class_info)
        if factory:
            return factory
        module_end = class_info.rindex('.')
        if module_end == -1:
            return None
        module_name = class_info[0 : module_end]
        class_name = class_info[module_end + 1:]
        module_meta = __import__(module_name, globals(), locals(), [class_name])
        class_meta = getattr(module_meta, class_name)
        factory = class_meta()
        self.factorys[class_info] = factory
        return factory



