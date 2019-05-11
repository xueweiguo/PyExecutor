from Interpreter.CalculateFunction import *
from Interpreter.Complex import *


class CosFun (CalculateFunction):
	def get_name(self):
		return 'cos'

	def execute(self, context, paraList):
		if len(paraList) != 1:
			context.setErrorMessage(self.get_name(), R_string.error_invalid_parameter_count)
			return False
		para = paraList[0]
		if para.i:
			context.setErrorMessage(self.get_name(), R_string.error_invalid_date_type)
			return False
		result = math.cos(para.r)
		context.setCurrentResult(Complex(result))
		return True
