from UmlStateDiagram.UsdStartPoint import *
from UmlStateDiagram.UsdEndPoint import *
from UmlStateDiagram.UsdConnector import *
from UmlStateDiagram.State import *
from UmlStateDiagram.StateMachine import *
from UmlStateDiagram.Choice import *

import sys
sys.path.append('..')
from ExFramework.ExComponentFactory import *

class UsdComponentFactory(ExComponentFactory):
    #构建起始点
    def make_initial(self):
        return UsdStartPoint('Initial')
    #构建终止点
    def make_final(self):
        return UsdEndPoint('Final')
    #添加链接线
    def make_connector(self):
        return UsdConnector('')
    #返回支持的要素类型
    def element_types(self):
         return ['State', 'StateMachine', 'Choice']
    #构建要素
    def make_element(self, index):
        if index==0:
            return State('Stata')
        elif index==1:
            return StateMachine('StateMachine')
        elif index==2:
            return Choice('Choice')
 
