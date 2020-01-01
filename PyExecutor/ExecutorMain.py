import sys
import os

# 准备命令行执行时需要的系统路径
cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)

from Foundation.Dialog import TopWnd
from Framework.SelectDiagramType import SelectDiagramType
from PyExecutor.ExecutorWnd import ExecutorWnd

# 导入Fbd功能
from FunctionBlock.Factories import fbd_register
# 导入小家电控制功能
from ElectricCooker.Factories import ecd_register

if __name__ == '__main__':
    fbd_register()
    ecd_register()
    dialog = TopWnd(SelectDiagramType())
    dialog.mainloop()
    main_wnd = ExecutorWnd('PyExecutor V0.1')
    main_wnd.mainloop()





