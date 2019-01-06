from Interpreter.CalculateFunction import *
from Interpreter.Complex import *

class SinhFun (CalculateFunction):
	def getName(self):
		return "sinh"

	def execute(self, paraList, context):
		if len(paraList) != 1:
			context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
			return False
		para = paraList[0]
		if para.i:
			context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
			return False

		result = math.sinh(para.r)
		context.setCurrentResult(Complex(result))
		return True
