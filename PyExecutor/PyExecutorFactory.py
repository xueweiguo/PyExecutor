import sys
sys.path.append('..')

from ExFramework.ExNote import *

class PyExecutorFactory(object):
    _instance = None

    def __new__(cls):
        if not PyExecutorFactory._instance:
            PyExecutorFactory._instance = super(PyExecutorFactory, cls).__new__(cls)
            PyExecutorFactory._instance.element_dict = {}
            cls._instance.type_set = set()
        return PyExecutorFactory._instance

    def __init__(self):
        pass

    def registerElementFactory(self, mode, factory):
        self.element_dict[mode] = factory
        self.type_set.add(mode)
        print(self.element_dict)

    def elementFactory(self):
        key = str(sys.argv[1])
        return self.element_dict[key]

    def modes(self):
        for m in self.type_set:
            print(m)

