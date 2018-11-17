import sys

#sys.path.append('..')
from ExFramework.ExComponentFactory import *
from ExFramework.ExJsonEncoder import *
from PyExecutorFactory import *

from ElectricCooker.EcInitial import *
from ElectricCooker.EcFinal import *
from ElectricCooker.EcConnector import *
from ElectricCooker.OpPanel import *
from ElectricCooker.TempSensor import *
from ElectricCooker.HeatingController import *
from ElectricCooker.Display import *
from ElectricCooker.Heater import *


class EcComponentFactory(ExComponentFactory):

    def __init__(self):
        PyExecutorFactory().registerElementFactory('ecd', self)

    # 添加链接线
    def makeConnector(self):
        return EcConnector('')

    def elementTypes(self):
        types = ['OpPanel', 'TempSensor', 'Controller', 'Display', 'Heater']
        parent_types = ExComponentFactory.elementTypes(self)
        for t in parent_types:
            types.append(t)
        return types

    def makeElement(self, type):
        if type=='Initial':
            return EcInitial('Initial')
        elif type=='Final':
            return EcFinal('Final')
        elif type=='OpPanel':
            return OpPanel('OpPanel')
        elif type=='TempSensor':
            return TempSensor('TempSensor')
        elif type=='Controller':
            return HeatingController('Controller')
        elif type=='Display':
            return Display('Display')
        elif type == 'Heater':
            return Heater('Heater')
        return ExComponentFactory.makeElement(self, type)

    # 系列化编码器
    def jsonEncoder(self):
        return ExJsonEncoder

EcComponentFactory()