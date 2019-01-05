from Interpreter.StandardFormatter import *
from Interpreter.R_string import *


class EvaluateContext:
	def __init__(self, context, engine):
		self.systemContext = context
		self.calculateEngine = engine
		self.errorMessage = ''
		self.resultStack = []
		self.customFunctionStack = None
		self.paraListStack = None
		self.formatter = None

	def getCalculateEngine(self):
		return self.calculateEngine

	def getSystemContext(self):
		return self.systemContext

	def getFunctionManager(self):
		return self.calculateEngine.functionManager

	def setCurrentResult(self, current):
		self.resultStack.pop()
		self.resultStack.append(current)

	def getCurrentResult(self):
		if len(self.resultStack):
			return self.resultStack[len(self.resultStack) - 1]
		else:
			return None

	def pushResult(self, complex):
		self.resultStack.append(complex)

	def popResult(self):
		if len(self.resultStack):
			return self.resultStack.pop()
		else:
			return None

	def clearResult(self):
		self.resultStack.clear()

	def getCustomNameStack(self):
		if(not self.customFunctionStack):
			self.customFunctionStack = []
		return self.customFunctionStack

	def getParaListStack(self):
		if(not self.paraListStack):
			self.paraListStack = []
		return self.paraListStack

	def pushCustomCall(self, funName, paraList):
		callStack = self.getCustomNameStack()
		if(callStack.index(funName) == -1):
			callStack.append(funName)
			self.paraListStack.append(paraList)
			return True
		else:
			self.setErrorMessage2(funName, R_string.error_self_call)
			return False

	def popCustomCall(self):
		callStack = self.getCustomNameStack()
		callStack.pop()
		self.paraListStack.pop()
		return True

	def getFormatter(self):
		if(not self.formatter):
			self.formatter = StandardFormatter(self.systemContext)
		return self.formatter
	
	def setFormatter(self, _formatter):
		self.formatter = _formatter

	def setErrorMessage1(self, message):
		self.errorMessage = message

	def setErrorMessage2(self, errorSource, errorId):
		self.errorMessage = errorSource + ":" + self.systemContext.getText(errorId)

	def getErrorMessage(self):
		return self.errorMessage
