import sys
#sys.path.append('..')

from PyExecuteWnd import *
from FunctionBlockDiagram.FbdExecutorFactory import *
from FunctionBlockDiagram.FbdSerializeFactory import *
from ElectricCooker.EcComponentFactory import *
from ElectricCooker.EcSerializeFactory import *
from PyExecutorFactory import *
from SelModeDlg import *

if __name__ == '__main__':
    main_wnd = PyExecuteWnd('PyExecutor V0.1')
    main_wnd.mainloop()


