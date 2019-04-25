from Interpreter.CalculateFunction import *
from Interpreter.Complex import *

class Log10Fun (CalculateFunction):
	def getName(self):
		return 'log10'

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
		context.setCurrentResult(Complex(math.log10(para.r)))
		return self.checkResult(context)
