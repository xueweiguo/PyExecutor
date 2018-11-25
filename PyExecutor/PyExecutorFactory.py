import sys
#sys.path.append('..')


class PyExecutorFactory(object):
    _instance = None

    def __new__(cls):
        if not PyExecutorFactory._instance:
            cls._instance = super(PyExecutorFactory, cls).__new__(cls)
            cls._instance.factory_dict = {}
            cls._instance.type_set = set()
            cls._instance.mode = None
        return PyExecutorFactory._instance

    def __init__(self):
        pass

    def register(self, mode, name, factory):
        self.factory_dict[self.factory_key(mode, name)] = factory
        self.type_set.add(mode)

    def factory(self, name):
        return self.factory_dict[self.factory_key(self.mode, name)]

    def factory_key(self, mode, name):
        return mode + ',' + name
