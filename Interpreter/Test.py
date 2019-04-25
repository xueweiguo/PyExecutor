#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from tkinter.filedialog import *

from Interpreter.CalculateEngine import *
from Interpreter.EvaluateContext import *
from Interpreter.SystemContext import *
import re
if __name__ == "__main__":
    # 初期状態
    engine = CalculateEngine(SystemContext())
    print(engine.calculate('3+4', False))
    '''
    str = r'((\.[0-9]+)|([0-9]+\.[0-9]*)|([0-9]+))'
    s = '1.0+2+.2+2.2'
    #s = 'one two one two'
    m = re.findall(str, s)
    print(m)
    # ['one', 'one']

    m = re.findall(r'([0-9]+)', s)
    print(m)

    m = re.match(str, s)
    print(m)
    '''