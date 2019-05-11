import math
from Interpreter.CalculateFunction import *
from Interpreter.Complex import *

class AtanFun(CalculateFunction):
    def get_name(self):
        return 'atan'

    def execute(self, context, paraList):
        if (len(paraList) != 1):
            context.setErrorMessage(self.get_name(), R_string.error_invalid_parameter_count)
            return False
        para = paraList[0]
        if (para.i != 0):
            context.setErrorMessage(self.get_name(), R_string.error_invalid_date_type)
            return False

        context.setCurrentResult(Complex(math.atan(para.r)))
        return self.checkResult(context)
