from Interpreter.CalculateFunction import *
from Interpreter.Complex import *

class CoshFun (CalculateFunction):
	def getName(self):
		return 'cosh'

	def execute(self, paraList):
		if len(paraList) != 1:
			context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
			return False
		para = paraList[0]
		if(para.i != 0):
			context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
			return False

		result = math.cosh(para.r)
		context.setCurrentResult(Complex(result))
		return True
