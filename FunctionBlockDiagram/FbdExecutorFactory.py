from FunctionBlockDiagram.FbdConnector import *
from FunctionBlockDiagram.SinFun import *
from FunctionBlockDiagram.CosFun import *
from FunctionBlockDiagram.MathFun import *
from FunctionBlockDiagram.GraphFun import *
from FunctionBlockDiagram.CommInputFun import *
from FunctionBlockDiagram.CommOutputFun import *

#sys.path.append('..')

from PyExecutorFactory import *
from ExFramework.ExComponentFactory import *
from ExFramework.ExJsonEncoder import *

class FbdExecutorFactory(ExComponentFactory):
    def __init__(self):
        PyExecutorFactory().register('fbd', 'element', self)

    def make_connector(self, parent):
        return FbdConnector(parent).construct()

    def element_types(self):
        types = ['Sin', 'Cos', 'Math', 'ComIn', 'ComOut', 'Graph']
        parent_types = ExComponentFactory.element_types(self)
        for t in parent_types:
            types.append(t)
        return types

    def make_element(self, parent, type):
        element = None
        if type=='Sin':
            return SinFun(parent, 'Sin').construct()
        elif type=='Cos':
            return CosFun(parent, 'Cos').construct()
        elif type=='Math':
            return MathFun(parent, 'Math').construct()
        elif type == 'ComIn':
            return CommInputFun(parent).construct()
        elif type == 'ComOut':
            return CommOutputFun(parent).construct()
        elif type=='Graph':
            return GraphFun(parent, 'Graph').construct()
        return ExComponentFactory.make_element(self, parent, type)


FbdExecutorFactory()
