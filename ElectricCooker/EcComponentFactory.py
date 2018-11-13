from ElectricCooker.EcInitial import *
from ElectricCooker.EcFinal import *
from ElectricCooker.EcConnector import *
from ElectricCooker.OpPanel import *
from ElectricCooker.TempSensor import *
from ElectricCooker.HeatingController import *
from ElectricCooker.Display import *
from ElectricCooker.Heater import *

import sys
sys.path.append('..')
from ExFramework.ExComponentFactory import *

class EcComponentFactory(ExComponentFactory):
    #构建起始点
    def make_initial(self):
        return EcInitial('Initial')
    #构建终止点
    def make_final(self):
        return EcFinal('Final')
    #添加链接线
    def make_connector(self):
        return EcConnector('')
    #返回支持的要素类型
    def element_types(self):
         return ['OpPanel', 'TempSensor', 'HeatingController', 'Display', 'Heater']
    #构建要素
    def make_element(self, index):
        if index==0:
            return OpPanel('OpPanel')
        elif index==1:
            return TempSensor('TempSensor')
        elif index ==2:
            return HeatingController('HeatingController')
        elif index ==3:
            return Display('Display')
        elif index ==4:
            return Heater('Heater')
               

