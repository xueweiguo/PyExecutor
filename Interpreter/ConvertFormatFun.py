from Interpreter.CalculateFunction import *


class ConvertFormatFun(CalculateFunction):
	def __init__(self, name, formatter):
		self.funName = name
		self.complexFormatter = formatter

	def get_name(self):
		return self.funName

	def execute(self, paraList):
		if len(paraList) != 1:
			context.setErrorMessage(self.get_name(), R_string.error_invalid_parameter_count)
			return False

		para = paraList[0]
		context.setCurrentResult(para)
		context.setFormatter(self.complexFormatter)
		return self.checkResult(context)
