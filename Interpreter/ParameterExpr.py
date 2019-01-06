from Interpreter.TerminalExpr import *
from Interpreter.R_string import *

class ParameterExpr(TerminalExpr):
	@staticmethod
	def buildExpr(cls, context):
		token = context.tokenList.pop(0)
		return ParameterExpr(int(token.getContent()[1:]))

	def __init__(self, number):
		self.paraNumber = number

	def evaluate(self, context):
		customNameList = context.getCustomNameStack()
		if len(customNameList) > 0:
			paraList = context.getParaListStack().getLast()
			funName = customNameList.getLast()
			para = paraList.get(self.paraNumber - 1)
			if para:
				context.setCurrentResult(para)
				return True
			else:
				context.setErrorMessage(funName, R_string.error_invalid_parameter_count)
				return False
		else:
			para = "#%d".format(self.paraNumber)
			context.setErrorMessage(para, R_string.error_invalid_input)
			return False
