import math
from Interpreter.CalculateFunction import *
from Interpreter.Complex import *


class AverageFun(CalculateFunction):
	def get_name(self):
		return 'avg'

	def execute(self, context, paraList):
		if(len(paraList) == 0):
			context.setErrorMessage(self.get_name(), R_string.error_invalid_parameter_count)
			return False

		result = Complex(0)
		for c in paraList:
			result = Complex.add(result, c)

		result = Complex.div(result, Complex(len(paraList)))
		context.setCurrentResult(result)
		return self.checkResult(context)
