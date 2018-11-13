
# Tk8.0 style top-level window menus
import sys
sys.path.append('..')

from PyExecuteWnd import *
#from PyExecuteWnd1 import *
from ElectricCooker.EcComponentFactory import *
from FunctionBlockDiagram.FbdExecutorFactory import *
from UmlStateDiagram.UsdComponentFactory import *
from PyExecutorFactory import *

if __name__ == '__main__':
    main_wnd = PyExecuteWnd('PyExecutor V0.1')
    main_wnd.mainloop()


