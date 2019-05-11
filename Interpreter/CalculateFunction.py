import abc
import math
from Interpreter.R_string import *

class CalculateFunction(metaclass=abc.ABCMeta):
    def checkResult(self, context):
        if math.isnan(context.getCurrentResult().r):
            context.setErrorMessage(self.get_name(), R_string.error_mathmatic_error)
            return False
        return True
    @abc.abstractmethod
    def get_name(self):
        return ''

    @abc.abstractmethod
    def execute(self, context, paraList):
        return False
