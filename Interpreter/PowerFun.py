from Interpreter.CalculateFunction import *
from Interpreter.Complex import *


class PowerFun (CalculateFunction):
	def getName(self):
		return "pow"

	def execute(self, paraList, context):
		if(len(paraList) != 2):
			context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
			return False
		x = paraList[0]
		if(x.i != 0):
			context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
			return False

		y = paraList[1]
		if(y.i != 0):
			context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
			return False

		context.setCurrentResult(Complex(math.pow(x.r, y.r)))
		return self.checkResult(context)
