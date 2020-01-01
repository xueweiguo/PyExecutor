from Framework.ComponentFactory import *

from FunctionBlock.FbdConnector import *
from FunctionBlock.FbdContext import *
from FunctionBlock.GeneratorFun import *
from FunctionBlock.FilterFun import *
from FunctionBlock.MathFun import *
from FunctionBlock.ValPanelFun import *
from FunctionBlock.GraphFun import *
from FunctionBlock.CommInputFun import *
from FunctionBlock.CommOutputFun import *


class FbdComponentFactory(ComponentFactory):
    def __init__(self):
        # FactoryManager().register('fbd', 'element', self)
        ComponentFactory.__init__(self)

    def make_connector(self, cd, parent):
        return FbdConnector(cd).construct(parent)

    def element_types(self):
        types = ['Gentor', 'Filter', 'Math', 'ComIn', 'ComOut', 'ValPanel', 'Graph']
        types.extend(ComponentFactory.element_types(self))
        return types

    def make_element(self, cd, parent, type):
        element = None
        if type == 'Gentor':
            return GeneratorFun(cd, 'Generator').construct(parent)
        elif type == 'Filter':
            return FilterFun(cd, 'Filter').construct(parent)
        elif type == 'Math':
            return MathFun(cd, 'Math').construct(parent)
        elif type == 'ComIn':
            return CommInputFun(cd).construct(parent)
        elif type == 'ComOut':
            return CommOutputFun(cd).construct(parent)
        elif type == 'ValPanel':
            return ValPanelFun(cd, 'ValPanel').construct(parent)
        elif type == 'Graph':
            return GraphFun(cd, 'Graph').construct(parent)
        return ComponentFactory.make_element(self, cd, parent, type)

    def make_context(self):
        return FbdContext()
