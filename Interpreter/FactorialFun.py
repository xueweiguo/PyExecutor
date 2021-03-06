from Interpreter.CalculateFunction import *
from Interpreter.Complex import *


class FactorialFun (CalculateFunction):
	def get_name(self):
		return 'n!'

	def execute(self, paraList):
		if len(paraList) != 1:
			context.setErrorMessage(self.get_name(), R_string.error_invalid_parameter_count)
			return False

		para = paraList[0]
		if para.i:
			context.setErrorMessage(self.get_name(), R_string.error_invalid_date_type)
			return False

		if (para.r < 1) or (para.r != math.floor(para.r)):
			context.setErrorMessage(self.get_name(), R_string.error_invalid_input)
			return False

		result = 1
		for i in range(1, int(para.r) + 1):
			result = result * i

		context.setCurrentResult(Complex(result))
		return True
