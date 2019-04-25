from Framework.FactoryManager import *
from Framework.BuilderFactory import *
from FunctionBlock.CppBuilder import *
from FunctionBlock.PythonBuilder import *


class FbdBuilderFactory(BuilderFactory):
    def __init__(self):
        BuilderFactory.__init__(self)
        #FactoryManager().register('fbd', 'builder', self)

    def builder_types(self):
        types = ['C++', 'Python']
        return types

    def make_builder(self, type):
        if type == 'C++':
            return CppBuilder()
        elif type == 'Python':
            return PythonBuilder()
        else:
            return None
