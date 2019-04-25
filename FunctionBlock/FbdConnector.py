import sys
sys.path.append('..')
from Framework.Connector import *

class FbdConnector(Connector):
     def __init__(self, parent=None):
         Connector.__init__(self, parent, '')



