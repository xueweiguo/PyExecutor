import sys
#sys.path.append('..')

from PyExecuteWnd import *
from FunctionBlockDiagram.FbdExecutorFactory import *
from ElectricCooker.EcComponentFactory import *
from PyExecutorFactory import *

if __name__ == '__main__':
    PyExecutorFactory().modes()
    main_wnd = PyExecuteWnd('PyExecutor V0.1')
    main_wnd.mainloop()


