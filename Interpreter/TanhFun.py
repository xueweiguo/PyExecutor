from Interpreter.CalculateFunction import *
from Interpreter.Complex import *


class TanhFun (CalculateFunction):
	def getName(self):
		return 'tanh'

	def execute(self, paraList, context):
		if len(paraList) != 1:
			context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
			return False
		para = paraList[0]
		if para.i != 0:
			context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
			return False

		result = math.tanh(para.r)
		context.setCurrentResult(Complex(result))
		return True
