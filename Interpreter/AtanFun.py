import math
from Interpreter.CalculateFunction import *
from Interpreter.Complex import *

class AtanFun(CalculateFunction):
    def getName(self):
        return 'atan'

    def execute(self, paraList, context):
        if (len(paraList) != 1):
            context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
            return False
        para = paraList[0]
        if (para.i != 0):
            context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
            return False

        context.setCurrentResult(Complex(math.atan(para.r)))
        return self.checkResult(context)
