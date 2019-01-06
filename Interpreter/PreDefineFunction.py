from Interpreter.CustomFunction import *


class PreDefineFunction(CustomFunction):
	def __init__(self, name, expr):
		CustomFunction.__init__(self, name)
		self.exprString = expr

	def getExprString(self):
		return self.exprString

