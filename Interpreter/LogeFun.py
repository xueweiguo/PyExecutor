from Interpreter.CalculateFunction import *
from Interpreter.Complex import *

class LogeFun (CalculateFunction):
	def getName(self):
		return "loge"

	def execute(self, paraList):
		if len(paraList) != 1:
			context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
			return False

		para = paraList[0]
		if(para.r < 0):
			context.setErrorMessage(self.getName(), R_string.error_invalid_input)
			return False

		if(para.i != 0):
			context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
			return False

		context.setCurrentResult(Complex(math.log(para.r)))
		return self.checkResult(context)

