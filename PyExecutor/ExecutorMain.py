import sys
import os

# 准备命令行执行时需要的系统路径
cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)

# 导入Fbd功能
from FunctionBlock.Factories import *
# 导入小家电控制功能
from ElectricCooker.Factories import *

from Foundation.Dialog import TopWnd
from PyExecutor.ExecutorWnd import *


if __name__ == '__main__':
    FactoryManager().mode = 'Function Block Diagram'
    dialog = TopWnd(SelectDiagramType())
    dialog.mainloop()
    main_wnd = ExecutorWnd('PyExecutor V0.1')
    main_wnd.mainloop()





