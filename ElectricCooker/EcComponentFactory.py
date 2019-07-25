from Framework.ComponentFactory import *

from ElectricCooker.EcConnector import *
from ElectricCooker.EcContext import *
from ElectricCooker.OpPanel import *
from ElectricCooker.TempSensor import *
from ElectricCooker.HeatingController import *
from ElectricCooker.Display import *
from ElectricCooker.Heater import *


class EcComponentFactory(ComponentFactory):
    def __init__(self):
        ComponentFactory.__init__(self)

    # 添加连接线
    def make_connector(self, cd):
        return EcConnector(cd).construct(None)

    def element_types(self):
        types = ['OpPanel', 'TempIn', 'Contr', 'Disp', 'Heater']
        parent_types = ComponentFactory.element_types(self)
        for t in parent_types:
            types.append(t)
        return types

    def make_element(self, cd, type):
        if type=='OpPanel':
            return OpPanel(cd, 'OpPanel').construct(None)
        elif type=='TempIn':
            return TempSensor(cd, 'TempSensor').construct(None)
        elif type=='Contr':
            return HeatingController(cd, 'Controller').construct(None)
        elif type=='Disp':
            return Display(cd, 'Display').construct(None)
        elif type == 'Heater':
            return Heater(cd, 'Heater').construct(None)
        return ComponentFactory.make_element(self, cd, type)

    def source_types(self):
        return None

    def make_context(self):
        return EcContext()

EcComponentFactory()