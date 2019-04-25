import abc
import math
from Interpreter.R_string import *

class CalculateFunction(metaclass=abc.ABCMeta):
    def checkResult(self):
        if math.isnan(context.getCurrentResult().r):
            context.setErrorMessage(self.getName(), R_string.error_mathmatic_error)
            return False
        return True
    @abc.abstractmethod
    def getName(self):
        return ''

    @abc.abstractmethod
    def execute(self, paraList):
        return False
