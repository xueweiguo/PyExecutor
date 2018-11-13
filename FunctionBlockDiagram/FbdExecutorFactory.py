from FunctionBlockDiagram.FbdStartPoint import *
from FunctionBlockDiagram.FbdEndPoint import *
from FunctionBlockDiagram.FbdConnector import *
from FunctionBlockDiagram.SinFun import *
from FunctionBlockDiagram.CosFun import *
from FunctionBlockDiagram.MathFun import *
from FunctionBlockDiagram.GraphFun import *

import sys
sys.path.append('..')

from PyExecutorFactory import *
from ExFramework.ExComponentFactory import *
from ExFramework.ExJsonEncoder import *

class FbdExecutorFactory(ExComponentFactory):
    def __init__(self):
        PyExecutorFactory().registerElementFactory('fbd', self)

    def makeConnector(self):
        return FbdConnector()

    def elementTypes(self):
        types = ['Sin', 'Cos', 'Math', 'Graph']
        parent_types = ExComponentFactory.elementTypes(self)
        for t in parent_types:
            types.append(t)
        return types

    def makeElement(self, type):
        if type=='Initial':
            return FbdStartPoint('Initial')
        elif type=='Final':
            return FbdEndPoint('Final')
        elif type=='Sin':
            return SinFun('Sin')
        elif type=='Cos':
            return CosFun('Cos')
        elif type=='Math':
            return MathFun('Math')
        elif type=='Graph':
            return GraphFun('Graph')
        return ExComponentFactory.makeElement(self, type)

    # 系列化编码器
    def jsonEncoder(self):
        return ExJsonEncoder


FbdExecutorFactory()
