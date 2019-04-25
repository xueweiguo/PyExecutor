from Interpreter.CalculateFunction import *
from Interpreter.Complex import *


class SinFun (CalculateFunction):
	def getName(self):
		return "sin"

	def execute(self, paraList):
		if len(paraList) != 1:
			context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
			return False
		para = paraList[0]
		if para.i:
			context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
			return False

		result = math.sin(para.r)
		context.setCurrentResult(Complex(result))
		return True
