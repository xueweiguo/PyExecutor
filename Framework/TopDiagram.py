from Framework.Diagram import *


class TopDiagram(Diagram):
    def __init__(self, cd=None, name=None, type=None):
        Diagram.__init__(self, None, name)

        self._dict = cd
        self.type = type
        self.factorys = dict()

    def construct(self, parent):
        Diagram.construct(self, parent)
        return self

    # 事件处理
    def handle_request(self, component, req, params=None):
        ret = None
        if req == 'get_factory':
            ret = self.__get_factory(params['type'])
        else:
            ret = Diagram.handle_request(self, component, req, params)
        return ret

    def __get_factory(self, class_info):
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





