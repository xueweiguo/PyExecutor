import sys
sys.path.append('..')

from ExFramework.ExNote import *

class PyExecutorFactory(object):
    _instance = None

    def __new__(cls):
        if not PyExecutorFactory._instance:
            PyExecutorFactory._instance = super(PyExecutorFactory, cls).__new__(cls)
            PyExecutorFactory._instance.__element_dict = {}
        return PyExecutorFactory._instance

    def __init__(self):
        pass

    def registerElementFactory(self, name, factory):
        self.__element_dict[name] = factory
        print(self.__element_dict)

    def elementFactory(self):
        key = str(sys.argv[1])
        return self.__element_dict[key]

