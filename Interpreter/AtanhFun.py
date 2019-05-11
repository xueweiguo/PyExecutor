import math
from Interpreter.CalculateFunction import *
from Interpreter.Complex import *


class AtanhFun(CalculateFunction):
	def get_name(self):
		return 'atanh'

	def execute(self, context, paraList):
		if len(paraList) != 1:
			context.setErrorMessage(self.get_name(), R_string.error_invalid_parameter_count)
			return False

		para = paraList[0]
		if(para.i != 0):
			context.setErrorMessage(self.get_name(), R_string.error_invalid_parameter_count)
			return False
		context.setCurrentResult(Complex((math.log(1 + para.r) - math.log(1 - para.r)) / 2))
		return self.checkResult(context)
