from Interpreter.CalculateFunction import *
from Interpreter.Complex import *
from Interpreter.R_string import *


class AcosFun(CalculateFunction):
    def getName(self):
        return 'acos'

    def execute(self, paraList, context):
        if(len(paraList) != 1):
            context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
            return False

        para = paraList[0]
        if(para.i != 0):
            context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
            return False

        context.setCurrentResult(Complex(math.acos(para.r)))
        return self.checkResult(context)
