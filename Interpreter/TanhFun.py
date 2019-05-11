from Interpreter.CalculateFunction import *
from Interpreter.Complex import *


class TanhFun (CalculateFunction):
	def get_name(self):
		return 'tanh'

	def execute(self, context, paraList):
		if len(paraList) != 1:
			context.setErrorMessage(self.get_name(), R_string.error_invalid_parameter_count)
			return False
		para = paraList[0]
		if para.i != 0:
			context.setErrorMessage(self.get_name(), R_string.error_invalid_date_type)
			return False

		result = math.tanh(para.r)
		context.setCurrentResult(Complex(result))
		return True
