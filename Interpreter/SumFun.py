from Interpreter.CalculateFunction import *
from Interpreter.Complex import *

class SumFun(CalculateFunction):
	def getName(self):
		return "sum"

	def execute(self, paraList):
		if len(paraList) == 0:
			context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
			return False
		result = Complex()
		for c in paraList:
			result = Complex.add(result, c)

		context.setCurrentResult(result)
		return self.checkResult(context)



