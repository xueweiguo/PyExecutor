#sys.path.append('..')
from ExFramework.ExComponentFactory import *
from ExFramework.ExJsonEncoder import *
from PyExecutorFactory import *

from ElectricCooker.EcConnector import *
from ElectricCooker.OpPanel import *
from ElectricCooker.TempSensor import *
from ElectricCooker.HeatingController import *
from ElectricCooker.Display import *
from ElectricCooker.Heater import *


class EcComponentFactory(ExComponentFactory):

    def __init__(self):
        PyExecutorFactory().register('ecd', 'element', self)

    # 添加链接线
    def make_connector(self):
        return EcConnector('')

    def element_types(self):
        types = ['OpPanel', 'TempSensor', 'Controller', 'Display', 'Heater']
        parent_types = ExComponentFactory.element_types(self)
        for t in parent_types:
            types.append(t)
        return types

    def make_element(self, type):
        if type=='OpPanel':
            return OpPanel('OpPanel')
        elif type=='TempSensor':
            return TempSensor('TempSensor')
        elif type=='Controller':
            return HeatingController('Controller')
        elif type=='Display':
            return Display('Display')
        elif type == 'Heater':
            return Heater('Heater')
        return ExComponentFactory.make_element(self, type)

EcComponentFactory()