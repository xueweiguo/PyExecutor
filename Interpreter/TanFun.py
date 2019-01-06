import math
from Interpreter.CalculateFunction import *
from Interpreter.Complex import *

class TanFun (CalculateFunction):
	MIN_NUMBER = 1e-15
	
	def getName(self):
		return "tan"

	def execute(self, paraList, context):
		if len(paraList) != 1::
			context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
			return False
		para = paraList[0]
		if(para.i != 0):
			context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
			return False

		cycles = math.floor(para.r / 2 / math.pi)
		if cycles < 0 :
			cycles = cycles + 1

		angle = para.r - cycles * 2 * math.pi
		if (math.fabs(angle - math.pi / 2) < self.MIN_NUMBER) \
				or (math.fabs(angle - math.pi * 3 / 2) < self.MIN_NUMBER):
			context.setErrorMessage(self.getName(), R_string.error_invalid_input)
			return False

		result = math.tan(angle)
		context.setCurrentResult(Complex(result))
		return True
