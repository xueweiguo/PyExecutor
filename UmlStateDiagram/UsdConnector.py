import sys
sys.path.append('..')
from ExFramework.ExConnector import *

class UsdConnector(ExConnector):
    def _init__(self, name):
        ExElement.__init__(self,name)



