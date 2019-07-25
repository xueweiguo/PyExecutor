#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from tkinter.filedialog import *

from Interpreter.Calculator import *
import os
if __name__ == "__main__":
    c = Calculator()
    print(c.calculate('100.0*sin(29+(23*6))+sqrt(cos(34*5))'))
    #eval('os.system(\'whoami\')')
