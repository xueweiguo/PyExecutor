import sys

from PyExecuteWnd import *
from FunctionBlockDiagram.FbdExecutorFactory import *
from FunctionBlockDiagram.FbdSerializeFactory import *
from ElectricCooker.EcComponentFactory import *
from ElectricCooker.EcSerializeFactory import *
from Interpreter.Complex import *

if __name__ == '__main__':
    c1 = Complex(1,2)
    c2 = Complex(2,3)
    s = Complex.add(c1,c2)
    print(s.i, s.r)
    main_wnd = PyExecuteWnd('PyExecutor V0.1')
    main_wnd.mainloop()


