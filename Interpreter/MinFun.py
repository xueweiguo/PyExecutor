from Interpreter.CalculateFunction import *
from Interpreter.Complex import *


class MinFun (CalculateFunction):
    def get_name(self):
        return 'min'

    def execute(self, context, para_list):
        if len(para_list) != 2:
            context.setErrorMessage(self.get_name(), R_string.error_invalid_parameter_count)
            return False
        x = para_list[0]
        y = para_list[1]
        if x.r < y.r:
            context.setCurrentResult(x)
        else:
            context.setCurrentResult(y)
        return self.checkResult(context)
