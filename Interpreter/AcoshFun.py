import math
from Interpreter.CalculateFunction import *
from Interpreter.Complex import *


class AcoshFun(CalculateFunction):
    def get_name(self):
        return 'acosh'

    def execute(self, context,paraList):
        if len(paraList) != 1:
            context.setErrorMessage(self.get_name(), R_string.error_invalid_parameter_count)
            return False

        para = paraList[0]
        if (para.i != 0):
            context.setErrorMessage(self.get_name(), R_string.error_invalid_date_type)
            return False

        if (para.r < 1):
            context.setErrorMessage(self.get_name(), R_string.error_invalid_input)
            return False

        value = math.sqrt((para.r + 1) / 2) + math.sqrt((para.r - 1) / 2)
        if (value == 0):
            context.setErrorMessage(self.get_name(), R_string.error_invalid_input)
            return False

        context.setCurrentResult(Complex(math.log(value) * 2))
        return self.checkResult(context)
